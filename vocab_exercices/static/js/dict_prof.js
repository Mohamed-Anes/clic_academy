document.getElementById("word-table").style.display = "none";


// selection de cas de la liste de mot 

var cells = document.querySelectorAll(".tablelistmot td");

cells.forEach(function(cell) {
  cell.addEventListener("click", function() {
    console.log("Clic sur la case :", cell.innerText);
  });
});


////////////////////////////////////////////

function ajouterElementsALaListe(mots) {
    var ul = document.getElementById('maListe');
     // Supprimer tous les éléments <li> existants
    while (ul.firstChild) {
      ul.removeChild(ul.firstChild);
    }
    document.getElementById("word-table").style.display = "none";
  
  
    for (var i = 0; i < mots.length; i++) {
      var li = document.createElement('li');
      li.appendChild(document.createTextNode(mots[i]));
      li.classList.add('li_class'); // Ajouter la classe CSS souhaitée
     
      ul.appendChild(li);
    }
  }
  
  function getdefinition() {
  
    var contenuRecherche = document.getElementById("search-input").value;
     // envoit une requet pour defintion
     // get definition de mot dns un liste 
     // 
     var listdefiniction=[" الأرضُ، مُؤَنَّثَةٌ: اسمُ جِنْسٍ، أو جَمْعٌ بِلا واحِدٍ، ولم يُسْمَعْ أرْضَةٌ، ج: أرْضاتٌ وأُرُوضٌ وأرَضُونَ وآراضٌ، والأراضِي غيرُ قِياسِيٍّ، وأسْفَلُ قَوائِمِ الدَّابَّةِ، وكُلُّ ما سَفَلَ، والزُّكامُ، والنُّفْضَةُ، والرِّعْدَةُ.",
     " لا أرضَ لكَ: كَلاَ أمَّ لَكَ",
     " أرضُ نُوحٍ: قرية بالبَحْرَيْنِ",
     " هو ابنُ أرْضٍ: غَريبٌ",
     " ابنُ الأرضِ: نَبْتٌ كأنه شَعْرٌ، ويُؤْكَلُ",
     " مَأرُوضُ: المَزْكومُ، أُرِضَ، ومن به خَبَلٌ من أهْلِ الأرضِ والجِنِّ، والمُحَرِّكُ رأسَهُ وجَسَدَه بِلا عَمْدٍ، والخَشَبُ أكَلَتْه الأرَضَةُ، لدُوَيبَّةٍ معروفة",
     " أرِضَتِ القَرْحَةُ: مَجِلَتْ، وفَسَدَتْ، كاسْتَأرضَتْ",
     " أرُضَتِ الأرضُ فهي أرضٌ أرِيضَةٌ: زَكِيَّةٌ، مُعْجِبَةٌ لِلْعَينِ، خَليقَةٌ لِلخيرِ",
     " أُرْضَةُ وإِرْضَةُ وإِرَضَةُ: الكَلأَ الكثيرُ",
     " أرَضَتِ الأرضُ: كثُرَ فيها",
     " أرَضْتُها: وجَدْتُها كذلك",
     " هو آرَضُهُمْ به: أجْدَرُهُمْ",
     " عريضٌ أريضٌ: إتباع، أو سَمينٌ",
     " أريضٌ أو يرِيضٌ: بلد، أو وادٍ",
     " إِراضُ: العِراضُ الوِساعُ، وبساطٌ ضَخْمٌ من صُوفٍ أو وَبَرٍ",
     " آرَضَهُ اللّهُ: أزْكَمَهُ",
     " تَأريضُ: أن تَرْعَى كَلأَ الأرضِ وتَرْتادَهُ، ونِيَّةُ الصومِ وتَهْيِئَتُهُ، وتَشْذيبُ الكلامِ وتَهْذيبُهُ، والتَّثْقِيلُ، والإِصْلاحُ، والتَّلْبيثُ، وأن تَجْعَلَ في السِّقاءِ لَبَناً أو ماءٌ أو سَمْناً أو رُبًّا لإِصْلاحِهِ",
     " تَأرُّضُ: التَّثَاقُلُ إلى الأرض، والتَّعَرُّضُ، والتَّصَدِّي، وتَمَكُّنُ النَّبْتِ من أن يُجَزَّ",
     " فَسيلٌ مُسْتَأرِضٌ: له عِرْقٌ في الأرضِ، فإِذا نَبَتَ على جِذْعِ أُمِّهِ، فهو الراكِبُ، ووَدِيَّةٌ مُسْتَأرِضَةٌ",
     
  ]

    ajouterElementsALaListe(listdefiniction)
  
  
    }
    
  function getexemple() {
     
      var contenuRecherche = document.getElementById("search-input").value;
       //
       // get definition de mot 
       //
      var list = [
            "وما كلّ أرض مثلُ أرضٍ هي الحمى …................. وَما كلّ نَبتٍ مثلُ نَبتٍ هوَ البانُ (شعر الشاعر:بهاء الدين زهير  )",
            "صَلَّى رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ صَلَاةَ الْخَوْفِ بِذِي قَرَدٍ أَرْضٍ مِنْ أَرْضِ بَنِي سُلَيْمٍ ، فَصَفَّ النَّاسُ خَلْفَهُ صَفَّيْنِ صَفٌّ مُوَازِي الْعَدُوِّ وَصَفٌّ خَلْفَهُ ، فَصَلَّى بِالصَّفِّ الَّذِي يَلِيهِ رَكْعَةً ، ثُمَّ نَكَصَ هَؤُلَاءِ إِلَى مَصَافِّ هَؤُلَاءِ ، وَهَؤُلَاءِ إِلَى مَصَافِّ هَؤُلَاءِ ، فَصَلَّى بِهِمْ رَكْعَةً أُخْرَى (حديث )",
            "رمتْ أرضٌ بها أرضاً فأرضاً ، …................. كنَبَذِ القَومِ صائبَة َ السّهامِ (شعر الشاعر: ابن المعتز  )",
            "إِنَّمَا يَزْرَعُ ثَلَاثَةٌ رَجُلٌ لَهُ أَرْضٌ فَهُوَ يَزْرَعُهَا أَوْ رَجُلٌ مُنِحَ أَرْضًا فَهُوَ يَزْرَعُ مَا مُنِحَ ، أَوْ رَجُلٌ اسْتَكْرَى أَرْضًا بِذَهَبٍ أَوْ فِضَّةٍ '' . مَيَّزَهُ إِسْرَائِيلُ ، عَنْ طَارِقٍ ، فَأَرْسَلَ الْكَلَامَ الْأَوَّلَ , وَجَعَلَ الْأَخِيرَ مِنْ قَوْلِ سَعِيدٍ . (حديث )",
            "نَهَى رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ عَنِ الْمُحَاقَلَةِ وَالْمُزَابَنَةِ ، وَقَالَ : إِنَّمَا يَزْرَعُ ثَلَاثَةٌ رَجُلٌ لَهُ أَرْضٌ فَهُوَ يَزْرَعُهَا ، وَرَجُلٌ مُنِحَ أَرْضًا فَهُوَ يَزْرَعُ مَا مُنِحَ ، وَرَجُلٌ اسْتَكْرَى أَرْضًا بِذَهَبٍ أَوْ فِضَّةٍ (حديث )",
        ];
      ajouterElementsALaListe(list);
    
    
      }
  
  function getantonim() {
     
        var contenuRecherche = document.getElementById("search-input").value;
         //
         // get definition de mot 
         //
        var list = [
    " أضداد جَثَمَتِ الطَّائِرَة على الأَرْض (فعل) أَقْلَعَتْ ، طارَتْ ، حَلَّقَتْ",
   " أضداد لقَطَ (أخذ من الأرض) (فعل) أَسْقَطَ ، أَطْرَبَ ، رَمى ، طَرَحَ ، قَذَفَ ، لَفَظَ",
   " أضداد غَدِقَت الأرض (فعل) أَجْدَبَتْ ، أَمْحَلَتْ ، أَقْحَلَتْ",
   " أضداد جَرزَت الأرضُ (مَحَلَت) (فعل) خَصَبَت ، أَخصَبت ، مرِعت ، أمرعَت",
   " أضداد جَحِدَتِ الأَرْضُ (يَبِسَتْ) (فعل) خَصِبَتْ ، أَخْصَبَتْ ، أَمْرَعَتْ",
   " أضداد حَطَّ (على الأرض) (فعل) طَارَ ، حَلَّقَ",
   " أضداد بَوَّرَ الأرض (فعل) زَرَعَها ، فَلَحَها ، حَرَثَها",
   " أضداد بارَت الأرض (فعل) زَرِعَت ، فَلِحَتْ ، حَرِثَت",
   " أضداد أَمْعَرَتِ الأَرْضُ (أَجْدَبَتْ) (فعل) مَرَعَتْ ، أَمْرَعَتْ ، خَصَبَت ، أَخْصَبَتْ ، أَكْلأَتْ",
  "  أضداد أَمْرَعَت الأرض (فعل) قَحِلَت ، أَقْحَلَت ، أَمْعَرَت ، جَدُبَت ، أَجْدَبَت ، جَحِدَت ، أَجْحَدَت ، قَحِطَت ، أَقْحَطَت ، مَحِلَت ، أَمْحَلَت ، جَرِزَت ، صَلَدَت ، جَنَشَت",
        ];
        ajouterElementsALaListe(list)
      
      
        }
  
        
  function getsynonim() {
     
    var contenuRecherche = document.getElementById("search-input").value;
     //
     // get synonime de mot 
     //
    var list = [
       " مرادفات أوسب ت الأرض (فعل): كَثُرَ عُشْبُهَا",
       " مرادفات بحر الأرض (فعل): شَقَّ-ها-",
      "  مرادفات برس الأرض (فعل): سَهَّلَ(ها) ، لَيَّنَ(ها",
      "  مرادفات بوّر (الأرض) (فعل): تَرَكَ(ها)-من دُون زَرع-",
" مرادفات رَكَّزَ في الأرض (فعل): شَتَلَ , غَرَسَ , نَصَبَ غَرْسَة",
       " مرادفات لقَطَ (أخذ من الأرض) (فعل): أَخَذَ , أَعْيَا , أَكَلَّ , أَمْسَكَ , إِلْتَقَطَ , تَنَاوَلَ",
       " مرادفات أثبت (في الأرض) (فعل): اِنْغَرَسَ",
       " مرادفات سقي من الأرض (اسم): ما يُسْقَى",
      "  مرادفات رفع عن الأرض (اسم): اِلْتِقَاط ، عُثُور(على الشيء",
       " مرادفات بور من الأرض (اسم): مَتْرُوكَة من دُون زَرع",
       " مرادفات بوار من الأرض (اسم): لَم تُزْرَع]"
    ]

    ajouterElementsALaListe(list)
  
  
    }

 

        ////////////////////
        // Exemple de données
        var conjugationData = {
            "أنا": {
              pastKnown: "قُلْتُ",
              presentKnown: "أَقُولُ",
              command: "قُلْ",
              pastUnknown: "قِيلْتُ",
              presentSubjunctive: "أَقُلْ",
              presentJussive: "أَقُولَ",
              presentUnknown: "يُقَالُ"
            },
            "نحن": {
              pastKnown: "قُلْنَا",
              presentKnown: "نَقُولُ",
              command: "قُولُوا",
              pastUnknown: "قِيلْنَا",
              presentSubjunctive: "نَقُولُ",
              presentJussive: "نَقُولَا",
              presentUnknown: "يُقَالُ"
            },
            "أنت": {
              pastKnown: "قُلْتَ",
              presentKnown: "تَقُولُ",
              command: "قُلْ",
              pastUnknown: "قِيلْتَ",
              presentSubjunctive: "تَقُلْ",
              presentJussive: "تَقُولَ",
              presentUnknown: "يُقَالُ"
            },
            "أنتِ": {
              pastKnown: "قُلْتِ",
              presentKnown: "تَقُولِينَ",
              command: "قُولِي",
              pastUnknown: "قِيلْتِ",
              presentSubjunctive: "تَقُلِي",
              presentJussive: "تَقُولِي",
              presentUnknown: "يُقَالُ"
            },
            "أنتما": {
              pastKnown: "قُلْتُمَا",
              presentKnown: "تَقُولَانِ",
              command: "قُولَا",
              pastUnknown: "قِيلْتُمَا",
              presentSubjunctive: "تَقُولَا",
              presentJussive: "تَقُولَانِّ",
              presentUnknown: "يُقَالُ"
            },
            "أنتم": {
              pastKnown: "قُلْتُمْ",
              presentKnown: "تَقُولُونَ",
              command: "قُولُوا",
              pastUnknown: "قِيلْتُمْ",
              presentSubjunctive: "تَقُولُوا",
              presentJussive: "تَقُولُوا",
              presentUnknown: "يُقَالُ"
            },
            "أنتن": {
              pastKnown: "قُلْتُنَّ",
              presentKnown: "تَقُلْنَ",
              command: "قُلْنَ",
              pastUnknown: "قِيلْتُنَّ",
              presentSubjunctive: "تَقُلْنَ",
              presentJussive: "تَقُلْنَ",
              presentUnknown: "يُقَالُ"
            },
            "هو": {
              pastKnown: "قَالَ",
              presentKnown: "يَقُولُ",
              command: "قُلْ",
              pastUnknown: "قِيلَ",
              presentSubjunctive: "يَقُلْ",
              presentJussive: "يَقُولَ",
              presentUnknown: "يُقَالُ"
            },
            "هي": {
              pastKnown: "قَالَتْ",
              presentKnown: "تَقُولُ",
              command: "قُلِي",
              pastUnknown: "قِيلَتْ",
              presentSubjunctive: "تَقُولُ",
              presentJussive: "تَقُولَ",
              presentUnknown: "تُقَالُ"
            },
            "هما": {
              pastKnown: "قَالَا",
              presentKnown: "يَقُولَانِ",
              command: "قُولَا",
              pastUnknown: "قِيلَا",
              presentSubjunctive: "يَقُولَا",
              presentJussive: "يَقُولَانِّ",
              presentUnknown: "يُقَالُ"
            },
            "هم": {
              pastKnown: "قَالُوا",
              presentKnown: "يَقُولُونَ",
              command: "قُولُوا",
              pastUnknown: "قِيلُوا",
              presentSubjunctive: "يَقُولُوا",
              presentJussive: "يَقُولُوا",
              presentUnknown: "يُقَالُ"
            },
            "هن": {
              pastKnown: "قُلْنَ",
              presentKnown: "يَقُلْنَ",
              command: "قُلْنَ",
              pastUnknown: "قِيلْنَ",
              presentSubjunctive: "يَقُلْنَ",
              presentJussive: "يَقُلْنَ",
              presentUnknown: "يُقَالُ"
            }
          };
          
function fillConjugationTable() {
            var table = document.getElementById("word-table");
            var pronouns = Object.keys(conjugationData);
          
            for (var i = 0; i < pronouns.length; i++) {
              var pronoun = pronouns[i];
              var conjugations = conjugationData[pronoun];
          
              var row = table.insertRow(i + 1);
              var pronounCell = row.insertCell(0);
              pronounCell.textContent = pronoun;
          
              row.insertCell(1).textContent = conjugations.pastKnown;
              row.insertCell(2).textContent = conjugations.presentKnown;
              row.insertCell(3).textContent = conjugations.command;
              row.insertCell(4).textContent = conjugations.pastUnknown;
              row.insertCell(5).textContent = conjugations.presentSubjunctive;
              row.insertCell(6).textContent = conjugations.presentJussive;
              row.insertCell(7).textContent = conjugations.presentUnknown;
            }
}
          
        
function getconjugaison(){


            var contenuRecherche = document.getElementById("search-input").value;
             //
             // get conjugaison de mot 
             //
             var ul = document.getElementById('maListe');
             // Supprimer tous les éléments <li> existants
            

            while (ul.firstChild) {
              ul.removeChild(ul.firstChild);
            }
            document.getElementById("word-table").style.display = "contents";
            fillConjugationTable();
    
           
}
          