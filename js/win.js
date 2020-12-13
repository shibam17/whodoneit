const dynamicText = function() {
    const windowWidth = window.innerWidth;
    const dynamicTextContainers = document.querySelectorAll('.sqs-dynamic-text-container');

    for (var el of dynamicTextContainers) {
        const elementWidth = el.offsetWidth; // element width
        const widthRatio = Math.floor(elementWidth / windowWidth * 100); // relative element width
        const existingRatio = el.getAttribute('data-width-ratio'); // 


        if (elementWidth == windowWidth || existingRatio == widthRatio) {
            console.log('carry on...');
            continue;
        }

        el.setAttribute('data-width-ratio', widthRatio);

        const dynamicTextEls = el.querySelectorAll('.sqs-dynamic-text');
        for (var el of dynamicTextEls) {
            el.style.fontSize = widthRatio + '%';
        }

        console.log('REPAINT!');

    }
};

dynamicText();

// Smart resize
(function() {
    const throttle = function(type, name, obj) {
        obj = obj || window;
        let running = false;
        const func = function() {
            if (running) { return; }
            running = true;
            requestAnimationFrame(function() {
                obj.dispatchEvent(new CustomEvent(name));
                running = false;
            });
        };
        obj.addEventListener(type, func);
    };

    throttle('resize', 'optimizedResize');
})();

// handle event
window.addEventListener('optimizedResize', function() {
    dynamicText();
});