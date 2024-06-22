# UniDive 1st Training School in Chișinău, Moldova
This is the repositrory for the [UniDive 1st Training School](https://unidive.lisn.upsaclay.fr/doku.php?id=meetings:other-events:1st_unidive_training_school) in Chișinău, Moldova, held on 8-12 July 2024. 

## Pre-requisites for the courses
We expect you to fulfill the pre-requisites for **at least** course 1 or course 2, 

### Necessary pre-requisites 
These prerequisites should be ready by the **1st of July**:
1. Create a [Github](https://github.com/signup) **and* [Gitlab](https://gitlab.com/users/sign_up) account if you don’t have one already
2. If you start a **new UD treebank** (see Course 3), think about the name following [these instructions](https://universaldependencies.org/release_checklist.html#new-language-or-treebank). **Send** the Github login, the name of the language, and a proposal of the name of the treebank to [Daniel Zeman](https://ufal.mff.cuni.cz/daniel-zeman).
3. Prepare you corpus to annotate
  * If you start a corpus **from scratch** - see the instructions how to prepare new data to annotate
  * If you already have an **on-going annotation** project, see how to adapt your data for the Training School
  
### Recommended prerequisites
If you want to make the most of the Training School, you may also read the publications recommended for each of the [[https://unidive.lisn.upsaclay.fr/doku.php?id=meetings:other-events:1st_unidive_training_school:courses#annotation_of_multiword_expressions_for_newcomers|courses]].


### How to prepare new data to annotate?
1. Source text selection - **license**
  * Select your source texts carefully so that they are **free from copyright** issues and you can freely redistribute your annotations in the future
  * Ideally such data would come from [public domain](https://en.wikipedia.org/wiki/Public_domain)
  * Legal issues concerning copyright vary from one country to another, so we can only give you hints but no universal rules
  * Good candidates for source texts are:
    * Texts published explicitly under [Creative Commons](https://search.creativecommons.org/), like Wikipedia
    * Literary texts written by authors who died at least 70 years ago. If you use translation of such texts, the same period applies also to the translator.
    * Already published corpora, with a known open license
2. Source data selection - **running text**
   If you wish to select only one or a few fragments of a larger text, choose sentences which **follow each other** (rather than randomly selected sentences), so that a larger context is available for each sentence.
3. Corpus for **Course 1** on dependency syntax
  * Prepare a text of about **10 sentences** is enough; no particular genre required
  * The corpus should include **translations** and **glosses**, so that discussion with the trainers and other trainees is feasible; some [morphological information](https://www.eva.mpg.de/lingua/pdf/Glossing-Rules.pdf) can also be provided for a start
  * It should be in the format illustrated in the [example spreadsheet](https://docs.google.com/spreadsheets/d/160pxZ33jGheBOSbJspDaXSbrWuW52nU49Y2aov7o8DU) (see the /Example sheet/)
  * It should be provided it in one of the two alternative ways:
    * adding a new sheet to the [example spreadsheet](https://docs.google.com/spreadsheets/d/160pxZ33jGheBOSbJspDaXSbrWuW52nU49Y2aov7o8DU)
    * preparing a .csv or .tsv file following the same instructions (see [examples](https://github.com/UniDive/2024-UniDive-Chisinau-training-school/tree/main/Course-1-dependency-syntax/1-prerequisites))
  * If you have data in other formats (like ELAN or equivalent), please contact Bruno.Guillaume@loria.fr and skahane@parisnanterre.fr as soon as possible; we will try to help you convert your data into a format suitable for annotation
4. Corpus for **Course 2** on MWE annotation 
  * Prepare a text of approximately **5 pages** (some 2500 words); literature is recommended but not compulsory
  * It would preferably concern a new language, a new dialect, or a new genre; by /new/ we mean not already covered in the [[https://gitlab.com/parseme/corpora/-/wikis/home#languages|PARSEME 1.3 corpus]]
  * It does not have to be the same text as for Course 1
  * It should be in the [CoNLL-U](https://universaldependencies.org/format.html) or [CUPT](https://multiword.sourceforge.net/cupt-format) format 
  * If you have just raw text, you may easily convert it to CoNLL-U by the following procedure
    * Go to the [UDPipe](https://lindat.mff.cuni.cz/services/udpipe/) service
    * Select a model for your language (if any), or for a close language (if any) or for a language with the same writing system
    * Paste your text, untick /Tag and Lemmatize/ and tick /Parse/, to only produce segmentation.
    * Click /Process Input/
    * Click /Save output file/ and save the file on your computer
  * Go to the [FLAT](https://flat.lisn.upsaclay.fr/) annotation platform 
  * Select /PILOT UNIDIVE 2024/ configuration
  * Enter the login and the password; they have been sent to you in a separate email 
  * [Upload the file](https://docs.google.com/document/d/1nLoyptr686FIJozdHJH9iJqwB5PgaZSTOlTKkuGeqcI/edit#heading=h.lih6ef6xum5x) to FLAT

### How to adapt existing data to annotate?
1. Corpus for **Course 1**
  * If you already have CoNLL-U files with glosses and translations (and other features), just make them ready
  * If you wish to extend an existing UD treebank, make sure you can modify a Github repository containing this corpus
2. Corpus for **Course 2**
  * If you wish to work on an already existing PARSEME corpus, you will have to **update its tagset**, so as to allow for annotating MWEs of all syntactic types (not only verbal ones)
  * If your corpus is in the `.cupt` format
    * Log in to FLAT using the /PILOT UNIDIVE 2024/ configuration
    * Create a new folder, e.g. `UniDive-Training-School`
    * [Upload the file](https://docs.google.com/document/d/1nLoyptr686FIJozdHJH9iJqwB5PgaZSTOlTKkuGeqcI/edit#heading=h.lih6ef6xum5x) your `.cupt` file to this folder
  * If your corpus is already on FLAT
    * export it to the `.cupt` format, log out from FLAT, before logging in again and uploading the file, as explained above

### If you cannot come with your own data
We will prepare text samples for you in English and Naija (a pidgin Creole, close to English). 

