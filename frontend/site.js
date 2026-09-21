console.log('Скрипт загружен!');

// Переменная для хранения токена
let authToken = null;

const loginSection = document.getElementById('loginSection');
const dataSection = document.getElementById('dataSection');
const loginStatus = document.getElementById('loginStatus');

// --- ЛОГИКА АВТОРИЗАЦИИ ---
document.getElementById('loginBtn').addEventListener('click', async () => {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    loginStatus.textContent = 'Проверка...';
    loginStatus.className = '';

    try {
        const response = await fetch('http://localhost:5000/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'Ошибка входа');
        }

        // Успешный вход
        authToken = data.token;
        loginStatus.textContent = 'Успешный вход!';
        loginStatus.className = 'success';
        
        // Прячем форму логина, показываем данные
        setTimeout(() => {
            loginSection.classList.add('hidden');
            dataSection.classList.remove('hidden');
        }, 500);

    } catch (error) {
        loginStatus.textContent = error.message;
        loginStatus.className = 'error';
    }
});

// --- ЗАГРУЗКА ДАННЫХ ---
document.getElementById('loadBtn').addEventListener('click', async () => {
    const resultDiv = document.getElementById('result');
    resultDiv.textContent = 'Загрузка...';

    try {
        const response = await fetch('http://localhost:5000/api/data', {
            method: 'GET',
            headers: {
                // Передаем токен в заголовке
                'Authorization': `Bearer ${authToken}`
            }
        });

        if (response.status === 401) {
            throw new Error('Сессия истекла или доступ запрещен');
        }
        if (!response.ok) throw new Error('Ошибка сети');

        const data = await response.json();

        let html = `<p><strong>${data.message}</strong></p><ul>`;
        data.items.forEach(item => {
            html += `<li>${item}</li>`;
        });
        html += '</ul>';
        resultDiv.innerHTML = html;

    } catch (error) {
        resultDiv.textContent = 'Ошибка: ' + error.message;
    }
});

// --- ВЫХОД ---
document.getElementById('logoutBtn').addEventListener('click', () => {
    authToken = null;
    document.getElementById('password').value = '';
    loginStatus.textContent = '';
    dataSection.classList.add('hidden');
    loginSection.classList.remove('hidden');
    document.getElementById('result').textContent = 'Нажмите кнопку';
});