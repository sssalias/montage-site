
const urlTime = '/form/time/get/'

const timeContainer = document.querySelector('#time')
const timeHiddenInput = document.querySelector('#time-hidden')
const dateHiddenInput = document.querySelector('#date-hidden')

timeContainer.addEventListener('click', e => {
    if (e.target.classList.contains('time-item')) {
        const lastElement = document.querySelector('.time-item__selected')
        console.log(lastElement);
        if (lastElement) {
            lastElement.classList.remove('time-item__selected')
            lastElement.classList.add('time-item__normal')
        }
        e.target.classList.remove('time-item__normal')
        e.target.classList.add('time-item__selected')
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
                const allClosed = Object.values(data).filter(el => el === true)

                let html = ''
                for (let item in data) {
                    if (data[item] === true) {
                        html += `<div class="time-item time-item__normal">${item}</div>`
                    }
                }
                if (allClosed.length === 0) {
                    timeContainer.classList.remove('time-container__grid')
                    timeContainer.classList.add('time-container__center')
                    html += `<h3>Нет свободных позиций(</h3>`
                } else {
                    timeContainer.classList.add('time-container__grid')
                    timeContainer.classList.remove('time-container__center')
                }
                dateHiddenInput.setAttribute('value', `${year}-${month}-${day}`)
                timeContainer.innerHTML = html
            })
    }
}
