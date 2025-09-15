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

if (typeof updateUnixTime === 'function') {
    updateUnixTime();
    setInterval(updateUnixTime, 1000);
}



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


function injectNav() {
    var container = document.querySelector('.container');
    if (!container) return;

    function computePrefixFromStylesheet() {
        try {
            var css = document.querySelector('link[rel="stylesheet"][href]');
            if (!css) return '';
            var cssHref = css.getAttribute('href') || '';
            var ups = (cssHref.match(/\.\.\//g) || []).length;
            return Array(ups + 1).join('../');
        } catch (_) {
            return '';
        }
    }

    function rewriteNavLinks(prefix) {
        try {
            var links = container.querySelectorAll('.left-sidemobile a, .left-sidedesktop a');
            links.forEach(function(a) {
                var hrefAttr = a.getAttribute('href');
                if (!hrefAttr) return;
                if (/^https?:\/\//i.test(hrefAttr)) return; // external
                if (hrefAttr.charAt(0) === '/') {
                    a.setAttribute('href', prefix + hrefAttr.slice(1));
                }
            });
        } catch (_) {}
    }

    function tryFetch(paths) {
        if (!paths.length) return Promise.reject();
        var next = paths[0] + (paths[0].indexOf('?') === -1 ? ('?v=' + Date.now()) : '');
        return fetch(next, { cache: 'no-cache' }).then(function(r) {
            if (!r.ok) throw new Error('HTTP ' + r.status);
            return r.text();
        }).catch(function() {
            return tryFetch(paths.slice(1));
        });
    }

    var pathsToTry = [
        '/nav.html',
        'nav.html',
        '../nav.html',
        '../../nav.html',
        '../../../nav.html'
    ];

    tryFetch(pathsToTry)
        .then(function(html) {
            var temp = document.createElement('div');
            temp.innerHTML = html;

            // Only remove existing nav after we have new content
            container.querySelectorAll('.left-sidemobile, .left-sidedesktop').forEach(function(n) { n.remove(); });

            var children = Array.prototype.slice.call(temp.children);
            for (var i = children.length - 1; i >= 0; i--) {
                container.insertBefore(children[i], container.firstChild);
            }

            // Rewrite root-absolute links to relative based on page depth
            var prefix = computePrefixFromStylesheet();
            rewriteNavLinks(prefix);
        })
        .catch(function() {
            // If all fetch attempts fail (e.g., opened via file://), synthesize the left-side nav
            // so pages work without a server.
            var prefix = computePrefixFromStylesheet();
            var leftMobile = document.createElement('div');
            leftMobile.className = 'left-sidemobile';
            leftMobile.innerHTML = ''+
                '<div class="author">' +
                    '<div class="nav">' +
                        '<div class="navwrap">' +
                            '<a href="' + prefix + 'index.html">Index</a>' +
                            '<a href="' + prefix + 'feed.xml">RSS</a>' +
                            '<a href="' + prefix + 'now/">Now</a>' +
                            '<a href="' + prefix + 'about/">About</a>' +
                            '<a href="' + prefix + 'contact/">Contact</a>' +
                        '</div>' +
                    '</div>' +
                '</div>' +
                '<div class="webring">' +
                    '<div><a href="https://ochowebr.ing">Ocho Webring</a></div>' +
                    '<div>' +
                        '<a href="https://glasson.pro/">Prev</a>' +
                        '<a href="https://ochowebr.ing/random">Random</a>' +
                        '<a href="https://graic.net">Next</a>' +
                    '</div>' +
                '</div>';

            var leftDesktop = document.createElement('div');
            leftDesktop.className = 'left-sidedesktop';
            leftDesktop.innerHTML = ''+
                '<div class="nav">' +
                    '<a href="' + prefix + 'index.html">Index</a><br>' +
                    '<a href="' + prefix + 'feed.xml">RSS</a><br>' +
                    '<a href="' + prefix + 'now/">Now</a><br>' +
                    '<a href="' + prefix + 'about/">About</a><br>' +
                    '<a href="' + prefix + 'contact/">Contact</a>' +
                '</div>' +
                '<div class="author">' +
                    '<a href="' + prefix + 'index.html">' +
                        '<div class="unix-time"></div>' +
                        '<div class="clock"></div>' +
                        '<div class="formatted-date"></div>' +
                        '<strong>Callan (101) Sheldon</strong>' +
                    '</a>' +
                    '<div class="webring" style="padding: 1em 1em 0 0;">' +
                        '<div><a href="https://ochowebr.ing">Ocho Webring</a></div>' +
                        '<a href="https://qlyoung.net">Prev</a>' +
                        ' | ' +
                        '<a href="https://ochowebr.ing/random">Random</a>' +
                        ' | ' +
                        '<a href="https://graic.net">Next</a>' +
                    '</div>' +
                '</div>';

            // Insert synthesized left side at the top of container
            container.insertBefore(leftDesktop, container.firstChild);
            container.insertBefore(leftMobile, container.firstChild);
            // Ensure any root-absolute leftovers get rewritten
            rewriteNavLinks(prefix);
        });
}

document.addEventListener('DOMContentLoaded', injectNav);
