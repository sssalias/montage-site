
const urlTime = '/form/time/get/'

const timeContainer = document.querySelector('#time')
const timeHiddenInput = document.querySelector('#time-hidden')
const dateHiddenInput = document.querySelector('#date-hidden')

timeContainer.addEventListener('click', e => {
    if (e.target.classList.contains('time-item')) {
        timeHiddenInput.setAttribute('value', e.target.innerText)
    }
})

window.onload = function() {
    renderTime(celender.currYear, celender.currMonth +  1, celender.currDay)
    celender.getClick((year, month, day) => renderTime(year, month, day))

    function renderTime(year, month, day) {
        let url = urlTime + `${year}/${month}/${day}`
        axios
            .get(url)
            .then(res => {
                const data = res.data.time
                let html = ''
                for (let item in res.data.time) {
                    if (data[item] === true) {
                        html += `<div class="time-item time-item__normal">${item}</div>`
                    }
                }
                dateHiddenInput.setAttribute('value', `${year}-${month}-${day}`)
                timeContainer.innerHTML = html
            })
    }
}
