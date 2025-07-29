const sign_in_btn = document.querySelector('#sign-in-btn');
const sign_up_btn = document.querySelector('#sign-up-btn');
const container = document.querySelector('.container');

sign_up_btn.addEventListener('click', () => {
  container.classList.add('sign-up-mode');
});

sign_in_btn.addEventListener('click', () => {
  container.classList.remove('sign-up-mode');
});

var roleSelect = document.getElementById('etudiant');
var niveauField = document.getElementById('niveau-field');
var roleprof = document.getElementById("professeur")
roleSelect.addEventListener('change', function () {
  if (roleSelect.value === 'etudiant') {
    niveauField.style.display = 'block';
  } else {
    niveauField.style.display = 'none';
  }
});

roleprof.addEventListener('change', function () {
  if (roleprof.value === 'professeur') {
    niveauField.style.display = 'none';
  } else {
    niveauField.style.display = 'none';
  }
});
// Masquer le champ de niveau au chargement initial de la page
niveauField.style.display = 'none';


/******* */
//login

// function sendLogInInfo(data) {

//   fetch('/check_login', {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json'
//     },
//     body: JSON.stringify(data)
//   })
//     .then(response => {
//       if (response.ok) {
//         console.log('JSON data sent successfully');
//         return 0;
//       } else {
//         console.error('Error sending JSON data');
//         return 1;
//       }
//     })
//     .catch(error => {
//       console.error('Network error:', error);
//       return 1;
//     });

//   return 0;
// }

// var usernameInput = document.querySelector('input[type="text"]');
// var passwordInput = document.querySelector('input[type="password"]');
// var loginButton = document.querySelector('input[type="submit"]');

// loginButton.addEventListener('click', function (event) {
//   event.preventDefault(); // Empêcher le rechargement de la page

//   var usernameValue = usernameInput.value;
//   var passwordValue = passwordInput.value;

//   // Vérifier si tous les champs sont remplis
//   if (
//     usernameValue == '' ||
//     passwordValue == ''
//   ) {
//     window.alert('يرجى ملء جميع الحقول المطلوبة.');
//     return;
//   }

//   // send the data
//   data = {
//     username: usernameValue,
//     password: passwordValue
//   };

//   console.log(data)
//   res = sendLogInInfo(data);
//   if (res === 0) {
//     window.location.href = "/home";
//   }
// });


// sing up

function sendSignUpInfo(data) {

  fetch('/check_signup', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
    .then(response => {
      if (response.ok) {
        console.log('JSON data sent successfully');
        return 0;
      } else {
        console.error('Error sending JSON data');
        return 1;
      }
    })
    .catch(error => {
      console.error('Network error:', error);
      return 1;
    });

  return 0;
}

var form = document.querySelector('.sign-up-form');

form.addEventListener('submit', function (event) {
  event.preventDefault(); // Empêche le formulaire de se soumettre

  var roleSelect = document.querySelector('input[name="role"]:checked');
  var usernameInput = document.getElementById('username');
  var passwordInput = document.getElementById('password');
  var firstNameInput = document.querySelector('input[placeholder="الاسم الأول"]');
  var lastNameInput = document.querySelector('input[placeholder="الاسم الأخير"]');
  var birthdateInput = document.querySelector('input[placeholder="تاريخ الميلاد"]');
  var emailInput = document.querySelector('input[type="email"]');
  var niveauInput = document.querySelector('input[placeholder="المستوى الدراسي"]');
  var niveauField = document.querySelector('input[placeholder="المستوى"]');
  console.log(typeof (niveauField.value));
  // Vérifier si un rôle est sélectionné
  if (!roleSelect) {
    window.alert('يرجى تحديد دور.');
    return;
  }

  //   // Vérifier si tous les champs sont remplis
  if (
    usernameInput.value === '' ||
    passwordInput.value === '' ||
    firstNameInput.value === '' ||
    lastNameInput.value === '' ||
    birthdateInput.value === '' ||
    emailInput.value === ''
  ) {
    window.alert('يرجى ملء جميع الحقول المطلوبة.');
    return;
  }

  //   // Vérifier si le champ de niveau est obligatoire pour les étudiants
  if (roleSelect.value === 'etudiant' && niveauField && niveauField.offsetParent !== null && niveauField.value === '') {
    window.alert('يرجى ملء حقل المستوى الدراسي.');
    return;
  }

  //   // Vérifier la longueur du nom d'utilisateur
  if (usernameInput.value.length < 8) {
    window.alert('يجب أن يحتوي اسم المستخدم على 8 أحرف على الأقل.');
    return;
  }

  //   // Vérifier la longueur du mot de passe
  if (passwordInput.value.length < 8) {
    window.alert('يجب أن تحتوي كلمة المرور على 8 أحرف على الأقل.');
    return;
  }

  //   // Si toutes les validations passent, le formulaire est valide
  console.log('النموذج صالح. جارٍ تقديمه...');

  //   // Extraire les valeurs des champs du formulaire
  var firstName = firstNameInput.value;
  var lastName = lastNameInput.value;
  var dateOfBirth = birthdateInput.value;
  var my_username = usernameInput.value;
  var my_email = emailInput.value;
  var my_password = passwordInput.value;

  var niveau = null
  if (roleSelect.value === 'etudiant') {
    niveau = parseInt(niveauField.value);
  }


  data = {
    username: my_username,
    password: my_password,
    nom: lastName,
    prenom: firstName,
    date_naissance: dateOfBirth,
    email: my_email,
    type: roleSelect.value,
    niveau: niveau
  };

  console.log(data)

  res = sendSignUpInfo(data);
  if (res === 0) {
    window.location.href = "/home";
  }
  console.log('done : ', res)
});

  // Afficher les valeurs extraites dans la console
  // console.log("الاسم الأول: " + firstName);
  // console.log("الاسم الأخير: " + lastName);
  // console.log("تاريخ الميلاد: " + dateOfBirth);
  // console.log("اسم المستخدم: " + username);
  // console.log("البريد الإلكتروني: " + email);
  // console.log("كلمة المرور: " + password);
  // console.log("المستوى الدراسي: " + niveau);

  // Réinitialiser les champs du formulaire
  // roleSelect.checked = false;
  // usernameInput.value = '';
  // passwordInput.value = '';
  // firstNameInput.value = '';
  // lastNameInput.value = '';
  // birthdateInput.value = '';
  // emailInput.value = '';
  // niveauInput.value = '';
// });
