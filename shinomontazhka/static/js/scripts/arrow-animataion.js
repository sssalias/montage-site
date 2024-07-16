const domElement = document.querySelector('.offer-arrow-down-link')


anime({
    targets: domElement,
    translateY: -25,
    direction: 'alternate',
    loop: true,
    easing: 'easeInOutQuad'
})