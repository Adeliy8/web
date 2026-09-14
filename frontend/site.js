console.log('Скрипт загружен!');

document.getElementById('loadBtn').addEventListener('click', async () => {
    const resultDiv = document.getElementById('result');
    resultDiv.textContent = 'Загрузка...';

    try {
        const response = await fetch('http://localhost:5000/api/data');
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