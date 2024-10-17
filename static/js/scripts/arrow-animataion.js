const domElement = document.querySelector('.offer-arrow-down-link')
const scrollElement = window.document.scrollingElement || window.document.body || window.document.documentElement

anime({
    targets: domElement,
    translateY: -25,
    direction: 'alternate',
    loop: true,
    easing: 'easeInOutQuad'
})

domElement.addEventListener('click', () => {
    anime({
        targets: scrollElement,
        scrollTop: window.screen.height - 75 - 75,
        duration: 600,
        easing: 'easeInOutQuad'
      })
})
