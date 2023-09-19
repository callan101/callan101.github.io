function updateUnixTime() {
    const unixTimeElements = document.querySelectorAll(".unix-time");
    const now = new Date();
    const unixTime = Math.floor(now.getTime() / 1000); // Convert to seconds

    // Update all elements with the class "unix-time"
    unixTimeElements.forEach(element => {
        element.textContent = unixTime;
    });
}

function updateClock() {
    const clockElements = document.querySelectorAll(".clock");
    const now = new Date();

    const hours = now.getHours().toString().padStart(2, "0");
    const minutes = now.getMinutes().toString().padStart(2, "0");
    const seconds = now.getSeconds().toString().padStart(2, "0");
    const formattedTime = `${hours}:${minutes}:${seconds}`;

    // Update all elements with the class "clock"
    clockElements.forEach(element => {
        element.textContent = formattedTime;
    });
}

function formatYearMonthDay() {
    const formattedDateElements = document.querySelectorAll(".formatted-date");
    const now = new Date();

    const year = now.getFullYear();
    const month = now.getMonth() + 1;
    const day = now.getDate();
    const formattedDate = `${year}.${month}.${day}`;

    // Update all elements with the class "formatted-date"
    formattedDateElements.forEach(element => {
        element.textContent = formattedDate;
    });
}

formatYearMonthDay();
setInterval(formatYearMonthDay, 1000);

updateClock();
setInterval(updateClock, 1000);

updateUnixTime();
setInterval(updateUnixTime, 1000);
