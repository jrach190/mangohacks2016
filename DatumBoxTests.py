API_KEY = "2a13913dda346761765020c1f66e34f8"

import unittest
from DatumBox import DatumBox, DatumBoxError

#Data for tests
positive_review = """I hesitate to dip my toe in the turbulent waters of Kindle Fire HD customer reviews, but having owned the 32GB version for two weeks now my thoughts might be useful to some. I already own a Kindle 3G and a WiFi/3G Ipad, against which the Fire HD seems to be regularly compared against. The Kindle is primarily used to take books on holiday, and the Ipad is used at home (via WiFi) and on holiday (3G/WiFi in the UK, WiFi abroad) for e-mails and internet access. I bought the Fire HD primarily (I thought)as a colour Kindle 'plus' - the 'plus' being a second access point to e-mails and internet if my partner was using the Ipad. Out of the box, it is a lovely looking piece of kit. It is heavier than a Kindle, but not distressingly so. You can hold it in one hand to read comfortably. WiFi access was automatically set-up - all I had to do was enter a pass-key (on the side of my Sky router). I have Sky e-mail, and I had to enter manually a couple of pieces of info in setting this up, but I got these from the account info on the Ipad. The Wi-Fi signal is picked up strongly throughout the house by the Fire HD, better than the Ipad in some rooms.

As an e-reader, it is very pleasing. The screen display is excellent - clear, detailed and the touchscreen works really well. Indeed, I am finding myself using it at home to read books which I have never done with my 'old' Kindle 3G. I also downloaded photos from my partner's Facebook to try this facility out - very easy to do and the photos look fantastic. What has really surprised me, however, is that I am now tending to use the Fire HD for my primary internet and e-mail access. Both functions are easy to use and very intuitive, and it is just easier to carry the Fire HD around than the Ipad. I have always worried about taking the Ipad abroad because of its size, even though the ability to use WiFi abroad has been invaluable. It looks like the Ipad can stay at home now, as I have an e-reader and internet access in one machine.
I have also used the useful comments from other reviewers and downloaded a number of third-party Android app sites and used these, as well as the Amazon App site, to load a few useful applications without any problems whatsoever, including Dolphin browser, YouTube etc etc. (And I write as someone who can just about turn on a computer).
In summation - and very much my opinion - I am delighted with my Fire HD. It is a much more portable size than an Ipad, offers the functionality I need and looks and sounds lovely. It has completely exceeded my expectations and is very much (for me) an Ipad 'minus' rather than a Kindle 'plus'.
Hope this review is helpful to someone. """

negative_review = """Maybe I have missed something here but I don't think so. Many users will be aware that on occasions their Kindle Fire HD slows down to a crawl for no apparent reason. Here is the reason: When you have finished with an open app, It does NOT close. If you hit the home screen button, which is the seemingly obvious way to close an app, it is still there in the background, and if it is an app that uses resources, it will slow you down. If you have opened then "closed" several apps, they are still in memory. This is a blunder by Amazon. The only way to free up memory and CPU for certain is to laboriously open settings/more/apps/force shut down. This is an absurd way to have to properly close an app, and needs to be addressed urgently with an update."""


positive_tweet = """Also, @xDaniielle has understood she can't beat me playing GTA. So instead, she's grabbing a copy too. I have an amazing girlfriend :D"""

#The below tweet was not written by me, I would never say such a horrid thing.
negative_tweet = """Gah! I hate programming. Been pissing me off all day. Time to go sit on the sofa in a huff with a beer :("""

science_objective_text = """Tin is a chemical element with symbol Sn (for Latin: stannum) and atomic number 50. It is a main group metal in group 14 of the periodic table. Tin shows chemical similarity to both neighboring group-14 elements, germanium and lead, and has two possible oxidation states, +2 and the slightly more stable +4. Tin is the 49th most abundant element and has, with 10 stable isotopes, the largest number of stable isotopes in the periodic table. Tin is obtained chiefly from the mineral cassiterite, where it occurs as tin dioxide, SnO2."""

tech_subjective_text = """The only conclusion I can draw is that building a compelling application is far more important than choice of language. While PHP wouldn't be my choice, and if pressed, I might argue that it should never be the choice for any rational human being sitting in front of a computer, I can't argue with the results.
You've probably heard that sufficiently incompetent coders can write FORTRAN in any language. It's true. But the converse is also true: sufficiently talented coders can write great applications in terrible languages, too. It's a painful lesson, but an important one.
Why fight it? I say learn to embrace it. Join with me, won't you, in celebrating the next fifty years of glorious PHP code driving the internet. Just don't forget to call the maintain_my_will_to_live() PHP function every so often!"""

spam = """We wish to inform you that your email address was generated during the announcement of the Brazil 2014 world cup kick-off days and times for the world cup finals in Brazil and won \u00A31,800,000.00 GBP (One Million eight Hundred Thousand British Pound Sterling) Equivalent to ($2,820,551.53 USD), plus 2 tickets to watch the opening match to take place in Sao Paulo on June 12 at 5pm local time and the final, on July 13, at the iconic Maracana stadium (in Rio de Janeiro), at 4pm local time. The notification was send to you because your email address is active online and your reference number is Braz1894ESA. (No Ticket Were Sold), this was in conjunction with the South African LOC Team (Local Organizing Committee) FIFA2010 and Brazilian LOC (Local Organizing Committee) Team FIFA2014.Please note that your Ref: numbers falls within our Afro booklet representative office in Johannesburg South Africa as indicated in the verification data, since the last FIFA2010 world cup was held in South Africa."""

not_spam = """well, it's perfectly simple to increase velocity by 40% - just add 40% more points to all your estimates and do the same amount of work.
Given that this is so, it should be apparent why using velocity as a target is wrong, it just encourages inflated estimates.
A less glib answer is that your estimate already assumes you are going as fast as you can while doing everything correctly. The only way to really increase productivity by 40% is either to work overtime or to not do everything correctly. Both of these speed things up in the short term, but slow things down in the long term. And the long term in this case isn't very long, a month at the outside. The optimal long term strategy is to never go faster than your sustainable pace.
Peopleware talks eloquently about the issues of trying to force programmers into higher productivity , and is an often cited classic. But in general it won't be easy to change the mind of a manager that is going down the path that yours is. Your project may well be in trouble - this is certainly a red flag."""

adult_content = "Look at this porn"
non_adult_content = "I prefer cats to dogs"

basic_english_text = "Programming is telling a computer how to do certain things by giving it instructions. These instructions are called programs. A person who writes instructions is a computer programmer. These instructions come in different languages; they are called programming languages. Sometimes programmers use special software which helps them to make programs, and sometimes they use simpler software, called a text editor, which only gives them a place to type."

commercial_text = """Nexus 4 is the latest smartphone from Google. With cutting edge hardware, the latest version of Android, and the best Google apps  Nexus 4 puts the world's information at your fingertips."""

educational_text = """Your lungs are complex organs, but what they do is take a gas that your body needs to get rid of (carbon dioxide) and exchange it for a gas that your body can use (oxygen). In this article, we will take a close look at how your lungs work and how they keep your body's cells supplied with oxygen and get rid of the carbon dioxide waste. We will explain some of the conditions and diseases that make breathing harder and cause the lungsto fail. We will also explain why you can't hold your breath for a longtime and why you cough or hiccup. """

webpage_xhtml = """<?xml version="1.0" encoding="ASCII"?>

<!DOCTYPE html PUBLIC
  "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">

  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=ASCII" />
    <title>A Simple Example</title>
    
    
    <script type="text/javascript" src="./static/test.js"> </script>

    <link rel="stylesheet" type="text/css" href="../static/css/mainbody.css">
    <link rel="stylesheet" type="text/css" href="../static/css/header.css">
  </head>

  <body onload="foo()">

    <div id="header">
        <h1>Candylush Creations</h1>
        <div id="contact">
            <h2><span class="cmeth">Phone:</span> <span class="cdet">XXXXX XXXXX</span></h2>
            <h2><span class="cmeth">Email:</span> <span class="cdet">candylushcreations@yahoo.com</span></h2>
        </div>
        <div id="nav">
            <ul>
                <li>Home</li> -
                <li>Pick A Tree</li> -
                <li>FAQ</li> - 
                <li>View Basket (0)</li>
            </ul>
        </div>
    </div>
    <div id="content">
        <div id="buyit">
            <div id="bpics">
                <div id="photos">blah</div>
            </div>
            <div id="btext">
                <table id="buyinfo">
                    <tr>
                        <td class="size">Small</td><td>&#65533;xx.xx</td><td class="input">|______|</td>
                    </tr>
                    <tr>
                        <td class="size">Medium</td><td>&#65533;xx.xx</td><td class="input">|______|</td>
                    </tr>
                    <tr>
                        <td class="size">Large</td><td>&#65533;xx.xx</td><td class="input">|______|</td>
                    </tr>
                </table>
                <span id="add">Add To Basket</span>
            </div>
        </div>
        <div id="about">
            <h2> About Us</h2>
            <p> Something blah blah doo doo doo oop booop boopity boopoop blah blah doo doo doo oop booop boopity boopoop blah blah doo doo doo oop booop boopity boopoop blah blah doo doo doo oop booop boopity boopoop blah blah doo doo doo oop booop boopity boopoop blah blah doo doo doo oop booop boopity boopoop</p>        
        </div>
    </div>

  </body>

</html>
"""


#Begin tests
datum_box = DatumBox(API_KEY)
bad_datum_box = DatumBox("This-API-key-is-not-valid-(hopefully)")
    

class TestSentimentAnalysis(unittest.TestCase):
   
    def test_positive_review(self):
        self.assertEqual(datum_box.sentiment_analysis(positive_review), "positive")
        
    def test_negative_review(self):
        self.assertEqual(datum_box.sentiment_analysis(negative_review), "negative")
        
    def test_bad_api_key(self):
        self.assertRaises(DatumBoxError, bad_datum_box.sentiment_analysis, positive_review)
        
class TestTwitterSentimentAnalysis(unittest.TestCase):
    def test_positive_tweet(self):
        self.assertEqual(datum_box.twitter_sentiment_analysis(positive_tweet), "positive")
        
    def test_negative_tweet(self):
        self.assertEqual(datum_box.twitter_sentiment_analysis(negative_tweet), "negative")

class TestSubjectivityAnalysis(unittest.TestCase):
    def test_objective_text(self):
        self.assertEqual(datum_box.is_subjective(science_objective_text), False)
        
    def test_subjective_text(self):
        self.assertEqual(datum_box.is_subjective(tech_subjective_text), True)

class TestTopicClassification(unittest.TestCase):
    def test_tech_text(self):
        self.assertEqual(datum_box.topic_classification(tech_subjective_text), "Computers & Technology")
    
    def test_science_text(self):
        self.assertEqual(datum_box.topic_classification(science_objective_text), "Science")

class TestSpamDetection(unittest.TestCase):
    def test_spam(self):
        self.assertEqual(datum_box.is_spam(spam), True)
        
    def test_nospam(self):
        self.assertEqual(datum_box.is_spam(not_spam), False)
        
class TestAdultContentDetection(unittest.TestCase):
    def test_adult(self):
        self.assertEqual(datum_box.is_adult_content(adult_content), True)
        
    def test_non_adult(self):
        self.assertEqual(datum_box.is_adult_content(non_adult_content), False)

class TestReadabiltyAssesment(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(datum_box.readability_assessment(basic_english_text), "basic")
        

class TestLanguageDetection(unittest.TestCase):
    def test_english(self):
        self.assertEqual(datum_box.detect_language(basic_english_text), "en")
        
class TestCommercialDetection(unittest.TestCase):
    def test_commercial(self):
        self.assertEqual(datum_box.is_commercial(commercial_text), True)
        

class TestEducationalDetection(unittest.TestCase):
    def test_educational(self):
        self.assertEqual(datum_box.is_educational(educational_text), True)
        
class TestKeywordExtract(unittest.TestCase):
    def test_keyword_extract(self):
        self.assertIn("cheese", datum_box.keyword_extract("This is some example text about cheese"));
        
class TestTextExtract(unittest.TestCase):
    def test_text_extract(self):
        extracted_text = datum_box.text_extract(webpage_xhtml)
        self.assertTrue("blah blah doo doo" in extracted_text)
        self.assertTrue("<html>" not in extracted_text)
        
class TestDocumentSimilarity(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(datum_box.document_similarity("This is some text", "This is some text"), 1)



if __name__ == '__main__':
    unittest.main()
