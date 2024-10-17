// const celenderContainer = document.querySelector('#celender')


// console.log(celenderContainer)

const celenderDate = document.querySelector('.celender-date')

var Cal = function(divId) {
    //Сохраняем идентификатор div
    this.divId = divId;
    // Дни недели с понедельника
    this.DaysOfWeek = [
      'Пн',
      'Вт',
      'Ср',
      'Чт',
      'Пт',
      'Сб',
      'Вс'
    ];
    // Месяцы начиная с января
    this.Months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'];
    //Устанавливаем текущий месяц, год
    var d = new Date();
    this.currMonth = d.getMonth();
    this.currYear = d.getFullYear();
    this.currDay = d.getDate();
    this.selected = new Date(this.currYear, this.currMonth, this.currDay)
  };
  // Переход к следующему месяцу
  Cal.prototype.nextMonth = function() {
    if ( this.currMonth == 11 ) {
      this.currMonth = 0;
      this.currYear = this.currYear + 1;
    }
    else {
      this.currMonth = this.currMonth + 1;
    }
    this.showcurr();
  };
  // Переход к предыдущему месяцу
  Cal.prototype.previousMonth = function() {
    if ( this.currMonth == 0 ) {
      this.currMonth = 11;
      this.currYear = this.currYear - 1;
    }
    else {
      this.currMonth = this.currMonth - 1;
    }
    this.showcurr();
  };
  // Показать текущий месяц
  Cal.prototype.showcurr = function() {
    this.showMonth(this.currYear, this.currMonth);
  };
  Cal.prototype.getClick = function(render) {
    const block = document.getElementById(this.divId)
    block.addEventListener('click', event => {
      if (event.target.className === 'not-active') {
        // TODO: logic here!!!!!!!
        const el = document.querySelector('span.active')
        if (el) {
          el.classList.remove('active')
          el.classList.add('not-active')
        }
        event.target.classList.remove('not-active')
        event.target.classList.add('active')
        const selectedDay = event.target.innerText
        const selectedDate = new Date(this.currYear, this.currMonth + 1, selectedDay)
        render(this.currYear, this.currMonth + 1, selectedDay)
      }
    })
  }
  // Показать месяц (год, месяц)
  Cal.prototype.showMonth = function(y, m) {
    var d = new Date()
    // Первый день недели в выбранном месяце 
    , firstDayOfMonth = new Date(y, m, 7).getDay()
    // Последний день выбранного месяца
    , lastDateOfMonth =  new Date(y, m+1, 0).getDate()
    // Последний день предыдущего месяца
    , lastDayOfLastMonth = m == 0 ? new Date(y-1, 11, 0).getDate() : new Date(y, m, 0).getDate();
    var html = '<table>';
    // Запись выбранного месяца и года
    html += '<thead><tr>';
    // html += '<td colspan="7">' + this.Months[m] + ' ' + y + '</td>';
    html += '</tr></thead>';
    // заголовок дней недели
    html += '<tr class="days">';
    celenderDate.innerHTML = this.Months[m] + ' ' + y
    for(var i=0; i < this.DaysOfWeek.length;i++) {
      html += '<td>' + this.DaysOfWeek[i] + '</td>';
    }
    html += '</tr>';
    // Записываем дни
    var i=1;
    do {
      var dow = new Date(y, m, i).getDay();
      // Начать новую строку в понедельник
      if ( dow == 1 ) {
        html += '<tr class="counts">';
      }
      // Если первый день недели не понедельник показать последние дни предыдущего месяца
      else if ( i == 1 ) {
        html += '<tr>';
        var k = lastDayOfLastMonth - firstDayOfMonth+1;
        for(var j=0; j < firstDayOfMonth; j++) {
          html += '<td class="not-current">' + k + '</td>';
          k++;
        }
      }
      // Записываем текущий день в цикл
      var chk = new Date();
      var chkY = chk.getFullYear();
      var chkM = chk.getMonth();
      if (chkY == this.currYear && chkM == this.currMonth && i == this.currDay) {
        html += '<td class="today">' + `<span class="active">${i}</span>` + '</td>';
      } else {
        html += '<td class="normal">' + `<span class="not-active">${i}</span>` + '</td>';
      }
      // закрыть строку в воскресенье
      if ( dow == 0 ) {
        html += '</tr>';
      }
      // Если последний день месяца не воскресенье, показать первые дни следующего месяца
      else if ( i == lastDateOfMonth ) {
        var k=1;
        for(dow; dow < 7; dow++) {
          html += '<td class="not-current">' + k + '</td>';
          k++;
        }
      }
      i++;
    }while(i <= lastDateOfMonth);
    // Конец таблицы
    html += '</table>';
    // Записываем HTML в div
    document.getElementById(this.divId).innerHTML = html;
  };
  // При загрузке окна
  window.onload = function() {
  }
  // Получить элемент по id
  function getId(id) {
    return document.getElementById(id);
  }



// Начать календарь
var celender = new Cal("divCal");	
celender.showcurr();
// Привязываем кнопки «Следующий» и «Предыдущий»
getId('btnNext').onclick = function() {
  celender.nextMonth();
};
getId('btnPrev').onclick = function() {
  celender.previousMonth();
};
// celender.getClick()