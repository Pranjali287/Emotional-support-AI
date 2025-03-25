import random
from textblob import TextBlob
from googletrans import Translator


# Helper function for sentiment analysis
def analyze_sentiment(text, language='en'):
    """Analyze the sentiment of the given text."""
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    return sentiment_score


# Function to detect specific emotions based on sentiment and text keywords
def detect_emotion(text, sentiment_score, language='en'):
    """Detect specific emotions like anger, irritation, joy, sadness, etc."""
    # Emotion keywords for different languages (English, Telugu, Kannada, Tamil, Hindi, Marathi)
    emotions_keywords = {
        'en': {
            'anger': ['mad', 'angry', 'rage', 'furious', 'fury'],
            'irritation': ['irritated', 'bothered', 'annoyed', 'fed up', 'cant'],
            'sadness': ['sad', 'depressed', 'hopeless', 'down', 'empty', 'bad', 'cry', 'crying'],
            'joy': ['happy', 'excited', 'joyful', 'elated', 'cheerful'],
            'motivation': ['useless', 'careless', 'failed', 'worthless', 'hopeless', 'ineffective']
        },
        'te': {  # Telugu
            'anger': ['కోపం', 'కోత', 'గ్రోధం', 'ఆగ్రహం'],
            'irritation': ['అసహనం', 'చింత', 'కోపం'],
            'sadness': ['నొప్పి', 'దుఃఖం', 'కోపం'],
            'joy': ['ఆనందం', 'సంతోషం', 'ప్రసన్నత'],
            'motivation': ['పనిచేయకుండా', 'అసమర్థత']
        },
        'ta': {  # Tamil
            'anger': ['கோபம்', 'கோர்வு', 'கண்ணியம்'],
            'irritation': ['சரிவுகள்', 'அசம்பாவிதம்'],
            'sadness': ['துயரம்', 'பாதை', 'ஆபத்துகள்'],
            'joy': ['மகிழ்ச்சி', 'சந்தோசம்', 'நல்ல நாள்'],
            'motivation': ['அசமர்த்தம்', 'முயற்சியில்']
        },
        'kn': {  # Kannada
            'anger': ['ಕೋಪ', 'ಹರಳು', 'ಕ್ರೋಧ'],
            'irritation': ['ಹುಚ್ಚು', 'ಚಿಂತನೆ', 'ಕೋಪ'],
            'sadness': ['ದುಃಖ', 'ನೋವು', 'ಅನುಭವಿಸು'],
            'joy': ['ಆನಂದ', 'ಹರ್ಷ', 'ಚೇತನ'],
            'motivation': ['ಅನರ್ಹ', 'ಅಸ್ವೀಕಾರ', 'ಅಪರಾಧ']
        },
        'hi': {  # Hindi
            'anger': ['गुस्सा', 'आक्रोश', 'क्रोध', 'नाराज'],
            'irritation': ['चिढ़', 'निराश', 'तंग', 'घबराया'],
            'sadness': ['उदास', 'दुःख', 'रोना', 'अकेलापन'],
            'joy': ['खुश', 'संतुष्ट', 'उत्साहित', 'प्रसन्न'],
            'motivation': ['निराश', 'असफल', 'अव्यवस्थित', 'कायर']
        },
        'mr': {  # Marathi
            'anger': ['राग', 'क्रोध', 'आक्रोश', 'ताव'],
            'irritation': ['चिडचिड', 'आततायी', 'अस्वस्थ'],
            'sadness': ['दुःख', 'उदासी', 'वेदना', 'एकटा'],
            'joy': ['आनंद', 'आनंदी', 'सुखी', 'उत्साही'],
            'motivation': ['निराश', 'अविचार', 'असमर्थ']
        },
    }

    # Select the keyword list for the chosen language
    emotion_keywords = emotions_keywords.get(language, emotions_keywords['en'])

    # Check if any keywords match
    text_lower = text.lower()

    if any(keyword in text_lower for keyword in emotion_keywords['anger']):
        return 'anger'
    if any(keyword in text_lower for keyword in emotion_keywords['irritation']):
        return 'irritation'
    if any(keyword in text_lower for keyword in emotion_keywords['sadness']):
        return 'sadness'
    if any(keyword in text_lower for keyword in emotion_keywords['joy']):
        return 'joy'
    if any(keyword in text_lower for keyword in emotion_keywords['motivation']):
        return 'motivation'

    # If sentiment is highly negative, detect sadness or anger
    if sentiment_score < -0.3:
        return 'sadness' if 'sad' not in text_lower else 'anger'

    # If sentiment is highly positive, detect joy
    if sentiment_score > 0.3:
        return 'joy'

    return 'neutral'


# Class to handle user interactions and privacy
class EmotionalSupportCompanion:
    def _init_(self):
        self.users = []  # A list to store anonymized user stories

    def anonymize_story(self, story):
        """Anonymize the story by removing sensitive information."""
        return f"Anonymous User: {story}"

    def handle_emotion(self, emotion, language):
        """Handle different emotions with appropriate responses."""
        responses = {
            'joy': {
                'en': ["That's fantastic! Keep spreading that positive energy! You are an amazing person.",
                       "I'm so happy for you! You deserve to be happy and loved."],
                'te': ['అద్భుతం!', 'మీ ఆహ్లాదకరమైన శక్తిని పంచుతుండండి! మీరు అద్భుతమైన వ్యక్తి.'],
                'ta': ['அற்புதம்!', 'உங்கள் மகிழ்ச்சியான சக்தியை பரப்புங்கள்! நீங்கள் அரிய மனிதர்.'],
                'kn': ['ಅದ್ಭುತ!', 'ನಿಮ್ಮ ಸಂತೋಷದ ಶಕ್ತಿಯನ್ನು ಹಂಚಿಕೊಳ್ಳಿ! ನೀವು ಅದ್ಭುತ ವ್ಯಕ್ತಿ.'],
                'hi': ['यह शानदार है!', 'आप इस सकारात्मक ऊर्जा को फैलाते रहें! आप एक अद्भुत व्यक्ति हैं।'],
                'mr': ['हे अप्रतिम आहे!', 'तुम्ही ही सकारात्मक ऊर्जा पसरवत राहा! तुम्ही एक अद्भुत व्यक्ती आहात.'],
            },
            'anger': {
                'en': ["It sounds like you're really upset right now. Take a deep breath.",
                       "I'm sorry you're feeling this way. It's okay to be angry, but try to find peace."],
                'te': ['మీరు ఈ విధంగా బాధపడుతున్నట్లయితే నాకు క్షమించాలి, మీరు శాంతియుతంగా ఉండటానికి ప్రయత్నించండి.'],
                'ta': ['நீங்கள் இப்போது கோபமாக இருக்கின்றீர்கள் போல தெரிகிறது. ஆழமான மூச்சு எடுக்கவும்.'],
                'kn': ['ನೀವು ಈಗ ಕೋಪಗೊಂಡಿದ್ದೀರಿ ಎಂದರೆ ತೀವ್ರವಾಗಿ ಸಂತೋಷವಾಗದಿದ್ದರೂ, ತಾಳ್ಮೆಯಾಗಿ ಅನುಭವಿಸು.'],
                'hi': ['ऐसा लगता है कि आप अभी बहुत गुस्से में हैं। गहरी सांस लें।', 'मुझे खेद है कि आप ऐसा महसूस कर रहे हैं। गुस्सा होना ठीक है, लेकिन शांति पाने की कोशिश करें।'],
                'mr': ['तुम्ही आताच रागावलेले दिसता. गहरी श्वास घ्या.', 'तुम्ही असं वाटत आहात यासाठी मला दुःख आहे. राग येणं ठीक आहे, पण शांतता मिळवण्याचा प्रयत्न करा.'],
            },
            # Define more responses for each emotion in each language similarly...
        }

        return random.choice(responses.get(emotion, {}).get(language, ["I'm here for you, can you express more."]))

    def get_user_input(self):
        """Simulate interaction with a user by getting their input."""
        print("\nWelcome to the Emotional Support Companion! Let's talk.")
        print("Feel free to share your thoughts anonymously.")

        # Ask for language selection
        language = input("Please select a language (en/te/ta/kn/hi/mr): ").strip().lower()

        # Validate language
        if language not in ['en', 'te', 'ta', 'kn', 'hi', 'mr']:
            print("Sorry, we currently support only English, Telugu, Tamil, Kannada, Hindi, and Marathi.")
            return

        # Get the user's story or feelings
        user_story = input(f"How are you feeling today? (Share your story in {language}): ")

        # Analyze the sentiment of the input
        sentiment_score = analyze_sentiment(user_story, language)

        # Detect specific emotion based on the text and sentiment
        emotion = detect_emotion(user_story, sentiment_score, language)

        # Anonymize the story before sharing
        anonymized_story = self.anonymize_story(user_story)
        print(f"\nYour story has been shared anonymously: {anonymized_story}\n")

        # Handle the detected emotion
        response = self.handle_emotion(emotion, language)
        print(response)

        # Optionally, ask if the user wants to share another experience
        another_story = input("\nWould you like to share something else? (yes/no): ")
        if another_story.lower() == 'yes':
            self.get_user_input()
        else:
            print("\nThank you for sharing! We're here if you need to talk again.")


# Main execution
if __name__ == "_main_":
    companion = EmotionalSupportCompanion()
    companion.get_user_input()