// Random Password generator of n-length. Length must be greater than or equal to 4

function shuffle(myString) {
    const chars = myString.split('');
  
    // Fisher-Yates shuffle algorithm
    for (let i = chars.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [chars[i], chars[j]] = [chars[j], chars[i]];
    }
    const newString = chars.join('');
    return newString;
  }

function generatePassword(length) {

    if (length < 4) {
        return "Length must be equal or greater than 4 " ;
    }

    const uppercaseChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const lowercaseChars = 'abcdefghijklmnopqrstuvwxyz';
    const numericChars = '0123456789';
    const specialChars = '!@#$%^&*()_-+=<>?';

    const basepass = uppercaseChars[Math.floor(Math.random() * uppercaseChars.length)] + lowercaseChars[Math.floor(Math.random() * lowercaseChars.length)] + numericChars[Math.floor(Math.random() * numericChars.length)] + specialChars[Math.floor(Math.random() * specialChars.length)]
  
    const allChars = uppercaseChars + lowercaseChars + numericChars + specialChars;
  
    let password = '';
  
    for (let i = 0; i < length-4; i++) {
      const randomIndex = Math.floor(Math.random() * allChars.length);
      password += allChars[randomIndex];
    }
    return shuffle(password+basepass);
  }
  

console.log(generatePassword(8)) ;

  