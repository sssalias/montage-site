const url = 'http://127.0.0.1:8000/form/data/get'

const getServices = () => {
    axios
        .get(url)
        .then(res => {
            renderServiceTypes(res.data.services_list)
            serviceTypesContainer.addEventListener('change', e => {
                if (e.target.tagName.toLowerCase() === 'input') {
                    const id = e.target.getAttribute('id')
                    renderServices(res.data.services_list.filter(el => el.type_id === id)[0].services, res.data.radius_list)
                }
            })
            window.addEventListener('load', e => {
                renderServices(res.data.services_list[0].services, res.data.radius_list)
                // renderServices(res.data.services_list.filter(el => el.type_id === id)[0].services)
            })
        })
        .catch(err => console.log(err))
}

const serviceTypesContainer =  document.querySelector('#service-types')
const servicesContainer = document.querySelector('#services')

function renderServiceTypes(data) {
    let html = ''
    data.forEach( (el, i) => {
        html += `
            <label  class="service-label service-label__row">
                <input ${i === 0 ? "checked" : ""} name="service_type" type="radio" id="${el.type_id}">
                 <span>${el.type}</span>
            </label>
        `
    })

    serviceTypesContainer.innerHTML = html
}

function renderServices(data, radius) {


    let html = '<label class="service-label service-label__column select-label">'
    html += '<span>Выберите тип услуги из списка</span>'
    html += '<select class="form-select" name="service" id="">'
    data.forEach(el => {
        html += `<option>${el}</option>`
    })
    html += '</select>'
    html += '</label>'

    html += `
        <label class="service-label service-label__column select-label">
           <span>Выберите радиус</span>
           <select class="form-select" name="radius" id="">
        `
    radius.forEach(el => {
        html += `<option>R${el}</option>`
    })
    html += `
        </select>
        
    `

    servicesContainer.innerHTML = html
    
}


document.onload = getServices()