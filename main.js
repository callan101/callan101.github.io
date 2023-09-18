function updateUnixTime() {
    const unixTimeElement = document.getElementById("unix-time");
    const now = new Date();
    const unixTime = Math.floor(now.getTime() / 1000); // Convert to seconds
    unixTimeElement.textContent = unixTime;
}



function updateClock() {
    const clockElement = document.getElementById("clock");
    const now = new Date();

    // Get the hours, minutes, and seconds
    const hours = now.getHours().toString().padStart(2, "0");
    const minutes = now.getMinutes().toString().padStart(2, "0");
    const seconds = now.getSeconds().toString().padStart(2, "0");

    // Format the time in 24-hour clock format
    const formattedTime = `${hours}:${minutes}:${seconds}`;

    clockElement.textContent = formattedTime;
}

function formatYearMonthDay() {
    const formattedDateElement = document.getElementById("formatted-date");
    const now = new Date();

    const year = now.getFullYear(); // Get the year (e.g., 2023)
    const month = now.getMonth() + 1; // Get the month (0-11, so we add 1)
    const day = now.getDate(); // Get the day of the month (1-31)

    // Format the date as "year.month.day"
    const formattedDate = `${year}.${month}.${day}`;

    formattedDateElement.textContent = formattedDate;
}



formatYearMonthDay();
setInterval(formatYearMonthDay, 1000);


updateClock();
setInterval(updateClock, 1000);

updateUnixTime();
setInterval(updateUnixTime, 1000);