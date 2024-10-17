const body = document.querySelector('body')

const openButton = document.querySelector('#open-menu-button')
const closeButton = document.querySelector('#close-menu-button')
const modalWrapper = document.querySelector('#modal-wrapper')
const modalContainer = document.querySelector('#modal-container')

openButton.addEventListener('click', () => {
    body.style.overflowY = 'hidden'
    modalWrapper.classList.remove('modal-wrapper__inactive')
    modalWrapper.classList.add('modal-wrapper__active')
    modalContainer.classList.remove('modal-menu-container__inactive')
    modalContainer.classList.add('modal-menu-container__active')
})


closeButton.addEventListener('click', () => {
    body.style.overflowY = 'auto'
    modalWrapper.classList.remove('modal-wrapper__active')
    modalWrapper.classList.add('modal-wrapper__inactive')
    modalContainer.classList.remove('modal-menu-container__active')   
    modalContainer.classList.add('modal-menu-container__inactive') 
})
