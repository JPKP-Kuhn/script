function solution(number){
    // convert the number to a roman numeral
    while (number >= 0) {
          if (number >= 1000) {
              return 'M' + solution(number - 1000)
          } else if (number >= 900) {
              return 'CM' + solution(number - 900)
          } else if (number >= 500) {
              return 'D' + solution(number - 500)
          } else if (number >= 400) {
              return 'CD' + solution(number - 400)
          } else if (number >= 100) {
              return 'C' + solution(number - 100)
          } else if (number >= 90) {
              return 'XC' + solution(number - 90)
          } else if (number >= 50) {
              return 'L' + solution(number - 50)
          } else if (number >= 40) {
              return 'XL' + solution(number - 40)
          } else if (number >= 10) {
              return 'X' + solution(number - 10)
          } else if (number >= 9) {
              return 'IX' + solution(number - 9)
          } else if (number >= 5) {
              return 'V' + solution(number - 5)
          } else if (number >= 4) {
              return 'IV' + solution(number - 4)
          } else if (number >= 1) {
              return 'I' + solution(number - 1)
          } else {
              return ''
          }
      }
    
  }