/*
function updateUnixTime() {
    const unixTimeElements = document.querySelectorAll(".unix-time");
    const now = new Date();
    const unixTime = Math.floor(now.getTime() / 1000); // Convert to seconds

    // Update all elements with the class "unix-time"
    unixTimeElements.forEach(element => {
        element.textContent = unixTime;
    });
}
*/
function updateClock() {
    const clockElements = document.querySelectorAll(".clock");
    const now = new Date();

    const hours = now.getHours().toString().padStart(2, "0");
    const minutes = now.getMinutes().toString().padStart(2, "0");
    //const seconds = now.getSeconds().toString().padStart(2, "0");
    const formattedTime = `${hours}:${minutes}`;
    //const formattedTime = `${hours}:${minutes}:${seconds}`;

    // Update all elements with the class "clock"
    clockElements.forEach(element => {
        element.textContent = formattedTime;
    });
}

function formatYearMonthDay() {
    const formattedDateElements = document.querySelectorAll(".formatted-date");
    const now = new Date();

    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0'); // Ensure 2 characters for month
    const day = String(now.getDate()).padStart(2, '0'); // Ensure 2 characters for day
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



const videos = document.querySelectorAll('video');

function playClosestVideo() {
    const windowCenter = window.scrollY + window.innerHeight / 2;

    let closestVideo = videos[0];
    let closestDistance = Math.abs(windowCenter - videos[0].offsetTop - videos[0].offsetHeight / 2);

    videos.forEach(video => {
        const videoCenter = video.offsetTop + video.offsetHeight / 2;
        const distance = Math.abs(windowCenter - videoCenter);

        if (distance < closestDistance) {
            closestDistance = distance;
            closestVideo = video;
        }
    });

    videos.forEach(video => {
        if (video === closestVideo) {
            video.play();
        } else {
            video.pause();
        }
    });
}

