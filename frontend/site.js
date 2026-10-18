document.addEventListener('DOMContentLoaded', () => {
    const loginBox = document.getElementById('loginBox');
    const dataBox = document.getElementById('dataBox');
    const loginBtn = document.getElementById('loginBtn');
    const loadBtn = document.getElementById('loadBtn');
    const logoutBtn = document.getElementById('logoutBtn');
    const loginStatus = document.getElementById('loginStatus');
    const resultDiv = document.getElementById('result');

    // Адрес вашего Flask-сервера
    const API_URL = 'http://127.0.0.1:5000/api';

    // Проверка токена при загрузке страницы
    if (localStorage.getItem('token')) {
        showDashboard();
    }

    // --- ВХОД ---
    loginBtn.addEventListener('click', async () => {
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        loginStatus.textContent = 'Проверка данных...';
        loginStatus.className = 'status-msg';

        try {
            const response = await fetch(`${API_URL}/login`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password })
            });

            const data = await response.json();

            if (response.ok && data.token) {
                localStorage.setItem('token', data.token);
                loginStatus.textContent = 'Успешный вход!';
                loginStatus.classList.add('success');
                setTimeout(showDashboard, 500);
            } else {
                loginStatus.textContent = data.error || 'Неверный логин или пароль';
                loginStatus.classList.add('error');
            }
        } catch (error) {
            console.error('Ошибка входа:', error);
            loginStatus.textContent = 'Сервер недоступен. Запущен ли Python?';
            loginStatus.classList.add('error');
        }
    });

    // --- ЗАГРУЗКА ДАННЫХ ---
    loadBtn.addEventListener('click', async () => {
        const token = localStorage.getItem('token');
        resultDiv.innerHTML = '<span style="color: #94a3b8;">Загрузка данных с сервера...</span>';

        try {
            const response = await fetch(`${API_URL}/data`, {
                method: 'GET',
                headers: { 'Authorization': `Bearer ${token}` }
            });

            const data = await response.json();

            if (response.ok) {
                const items = data.items.map(item => `<li>${item}</li>`).join('');
                resultDiv.innerHTML = `<strong>${data.message}</strong><ul>${items}</ul>`;
            } else {
                resultDiv.innerHTML = `<span class="error">${data.error}</span>`;
                if (response.status === 401) logout(); // Если токен недействителен
            }
        } catch (error) {
            console.error('Ошибка данных:', error);
            resultDiv.innerHTML = `<span class="error">Ошибка соединения. Проверьте сервер.</span>`;
        }
    });

    // --- ВЫХОД ---
    logoutBtn.addEventListener('click', logout);

    function showDashboard() {
        loginBox.classList.add('hidden');
        dataBox.classList.remove('hidden');
        loginStatus.textContent = '';
    }

    function logout() {
        localStorage.removeItem('token');
        dataBox.classList.add('hidden');
        loginBox.classList.remove('hidden');
        document.getElementById('password').value = 'password123';
        loginStatus.textContent = 'Вы вышли из системы';
        loginStatus.className = 'status-msg';
        resultDiv.innerHTML = 'Нажмите кнопку выше, чтобы получить данные с сервера.';
    }
});