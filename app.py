import streamlit as st
import base64
import json
import os
import requests

# הגדרת כותרת הדף ואייקון
st.set_page_config(
    page_title="שגיא בר און - סדנאות והרצאות בינה מלאכותית",
    page_icon="🤖",
    layout="wide"
)

# CSS מותאם אישית
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700&display=swap');
    
    * {
        font-family: 'Heebo', sans-serif;
    }
    
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Heebo', sans-serif;
        font-weight: 700;
    }
    
    .main-header {
        text-align: center;
        color: #1E3A8A;
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .sub-header {
        text-align: center;
        color: #3B82F6;
        font-size: 1.5rem;
        margin-bottom: 2rem;
    }
    
    .workshop-card {
        background-color: #F3F4F6;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }
    
    .workshop-card:hover {
        transform: translateY(-5px);
    }
    
    .workshop-title {
        color: #1E3A8A;
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 10px;
    }
    
    .workshop-details {
        color: #4B5563;
        margin-bottom: 10px;
    }
    
    .contact-section {
        background-color: #E0F2FE;
        border-radius: 10px;
        padding: 20px;
        margin-top: 30px;
    }
    
    .profile-pic {
        border-radius: 50%;
        border: 5px solid #3B82F6;
        display: block;
        margin: 0 auto;
        max-width: 250px;
        cursor: pointer;
    }
    
    .rtl-text {
        direction: rtl;
        text-align: right;
    }
    
    .center-text {
        text-align: center;
    }
    
    .footer {
        text-align: center;
        padding: 20px;
        margin-top: 50px;
        color: #6B7280;
        font-size: 0.9rem;
    }
    
    .testimonial {
        font-style: italic;
        padding: 15px;
        background-color: #F0F9FF;
        border-right: 4px solid #3B82F6;
        margin: 20px 0;
    }
    
    .stButton>button {
        background-color: #3B82F6;
        color: white;
        font-weight: bold;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
    }
    
    .stButton>button:hover {
        background-color: #1E3A8A;
    }
    
    /* עיצוב התמונה עם מסגרת ואפקט לחיצה */
    img {
        border-radius: 10px;
        border: 3px solid #3B82F6;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    img:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 12px rgba(59, 130, 246, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# פונקציה לטעינת אנימציית Lottie
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# פונקציה להצגת קונפטי
def show_confetti():
    st_confetti(
        key="confetti",
        type="confetti",
        duration=3,
    )

# פונקציה לקבצי Lottie מקומיים
def load_lottie_file(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

# קובץ Lottie לבלונים או קונפטי
if os.path.exists("assets/balloons.json"):
    lottie_balloons = load_lottie_file("assets/balloons.json")
else:
    # אם הקובץ לא קיים, שימוש בURL חיצוני
    lottie_balloons = load_lottieurl("https://lottie.host/7a2b12f8-af2c-4159-80bc-c285fdc1a972/DYBZjYVj0E.json")

# כותרת ראשית
st.markdown('<h1 class="main-header">שגיא בר און</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="sub-header">סדנאות והרצאות בתחום הבינה המלאכותית</h2>', unsafe_allow_html=True)

# תמונת פרופיל במרכז
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # שימוש בקונטיינר כדי לעטוף את התמונה ולהפעיל אירוע לחיצה
    with st.container():
        # הצגת התמונה
        st.image("assets/profile.png", use_column_width=True)
        
        # כאשר לוחצים על כפתור "לחץ על התמונה", נפעיל את אנימציית הבלונים
        if st.button("לחץ על התמונה לאפקט מיוחד!"):
            # הפעלת אנימציית בלונים מובנית של Streamlit
            st.balloons()

# מידע כללי
st.markdown("""
<div class="rtl-text">
    <h2>ברוכים הבאים לאתר האישי שלי!</h2>
    <p>
        אני שגיא בר און, מומחה בינה מלאכותית וחוקר בתחום. אני מעביר סדנאות והרצאות ברחבי הארץ לארגונים, חברות, מוסדות חינוך וכנסים.
        הסדנאות וההרצאות שלי משלבות תיאוריה, ידע מעשי וחוויה אינטראקטיבית כדי להנגיש את עולם הבינה המלאכותית לכל קהל.
    </p>
</div>
""", unsafe_allow_html=True)

# סדנאות והרצאות
st.markdown('<h2 class="center-text">הסדנאות וההרצאות שלי</h2>', unsafe_allow_html=True)

# סדנה 1
st.markdown("""
<div class="workshop-card rtl-text">
    <div class="workshop-title">מבוא לבינה מלאכותית וכלי AI לעסקים</div>
    <div class="workshop-details">
        <strong>משך:</strong> 3 שעות<br>
        <strong>קהל יעד:</strong> מנהלים, יזמים ואנשי עסקים<br>
        <strong>תיאור:</strong> סדנה מעשית המציגה את הכלים העדכניים ביותר בתחום הבינה המלאכותית ואיך ניתן לשלב אותם בעסק. נלמד על ChatGPT, Midjourney, DALL-E ועוד כלים שיכולים להגביר את הפרודוקטיביות ולפתוח אפשרויות חדשות.
    </div>
</div>
""", unsafe_allow_html=True)

# סדנה 2
st.markdown("""
<div class="workshop-card rtl-text">
    <div class="workshop-title">פיתוח מודלים ויישומי AI: מתיאוריה למעשה</div>
    <div class="workshop-details">
        <strong>משך:</strong> יום מלא (8 שעות)<br>
        <strong>קהל יעד:</strong> מפתחים, מהנדסי תוכנה ואנשי דאטה<br>
        <strong>תיאור:</strong> סדנה מעמיקה המשלבת תיאוריה ותרגול מעשי בפיתוח מודלים ויישומי בינה מלאכותית. נלמד כיצד לבנות, לאמן ולשלב מודלים בפרויקטים אמיתיים תוך שימוש בכלים וספריות פופולריות כמו TensorFlow, PyTorch, Hugging Face ועוד.
    </div>
</div>
""", unsafe_allow_html=True)

# סדנה 3
st.markdown("""
<div class="workshop-card rtl-text">
    <div class="workshop-title">מהפכת ה-Generative AI והשפעתה על החברה</div>
    <div class="workshop-details">
        <strong>משך:</strong> שעתיים<br>
        <strong>קהל יעד:</strong> כל המעוניין<br>
        <strong>תיאור:</strong> הרצאה מרתקת על מהפכת ה-Generative AI והשפעתה על החברה, שוק העבודה, חינוך ואתיקה. נסקור את ההתפתחויות האחרונות בתחום ונדון באתגרים ובהזדמנויות שהטכנולוגיה החדשה מציבה בפנינו.
    </div>
</div>
""", unsafe_allow_html=True)

# סדנה 4
st.markdown("""
<div class="workshop-card rtl-text">
    <div class="workshop-title">AI לחינוך: כלים וטכניקות למורים ומרצים</div>
    <div class="workshop-details">
        <strong>משך:</strong> 4 שעות<br>
        <strong>קהל יעד:</strong> מורים, מרצים ואנשי חינוך<br>
        <strong>תיאור:</strong> סדנה מעשית המיועדת לאנשי חינוך, המציגה כלי AI שימושיים להוראה, יצירת תוכן לימודי, הערכה ומשוב. נלמד כיצד לשלב בינה מלאכותית בכיתה באופן אתי ויעיל, תוך פיתוח מיומנויות דיגיטליות אצל התלמידים.
    </div>
</div>
""", unsafe_allow_html=True)

# לקוחות ממליצים
st.markdown('<h2 class="center-text">לקוחות ממליצים</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="testimonial rtl-text">
        "הסדנה של שגיא שינתה את האופן שבו העסק שלנו מתנהל. הכלים שלמדנו חסכו לנו שעות עבודה ופתחו אפשרויות חדשות. ממליץ בחום!"
        <br><strong>- רונן כהן, מנכ"ל חברת טכנולוגיה</strong>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="testimonial rtl-text">
        "שגיא מעביר את הנושאים המורכבים בצורה ברורה ומרתקת. הסדנה הייתה משנה תפיסה עבור הצוות שלנו."
        <br><strong>- מיכל לוי, מנהלת משאבי אנוש</strong>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="testimonial rtl-text">
        "ההרצאה של שגיא הייתה אחת המרתקות שהיו לנו בכנס. משלב ידע מקצועי עם הומור ודוגמאות מעשיות."
        <br><strong>- דני אברהם, מנהל כנסים</strong>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="testimonial rtl-text">
        "כמורה, הסדנה פתחה בפניי עולם שלם של כלים ואפשרויות. התלמידים נהנים מהשיטות החדשות שהטמעתי בכיתה."
        <br><strong>- אורית שמיר, מורה לתקשורת</strong>
    </div>
    """, unsafe_allow_html=True)

# יצירת קשר
# יצירת קשר
st.markdown('<h2 class="center-text">יצירת קשר</h2>', unsafe_allow_html=True)
st.markdown('<p class="rtl-text">מעוניינים בהרצאה או סדנה? השאירו פרטים ואחזור אליכם בהקדם:</p>', unsafe_allow_html=True)

# שימוש ברכיבי Streamlit במקום HTML ישיר
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("שם מלא", key="name")
with col2:
    email = st.text_input("אימייל", key="email")

phone = st.text_input("טלפון", key="phone")
message = st.text_area("הודעה", height=100, key="message")

if st.button("שליחה", type="primary", key="send_btn"):
    # כאן תוכל להוסיף קוד שיטפל בשליחת הטופס
    st.success("תודה! ההודעה נשלחה בהצלחה. אחזור אליך בהקדם.")
    
# מידע נוסף
st.markdown("""
<div class="rtl-text" style="margin-top: 30px;">
    <h2>מידע נוסף</h2>
    <p>
        בנוסף לסדנאות וההרצאות, אני מציע גם שירותי ייעוץ אישי לארגונים המעוניינים לשלב בינה מלאכותית בתהליכי העבודה שלהם.
        ניתן לתאם פגישת ייעוץ ראשונית ללא התחייבות.
    </p>
</div>
""", unsafe_allow_html=True)

# לוח אירועים קרובים
st.markdown('<h2 class="center-text">אירועים קרובים</h2>', unsafe_allow_html=True)

events = [
    {"date": "15.06.2025", "title": "הרצאה: עתיד העבודה בעידן ה-AI", "location": "תל אביב", "time": "18:00-20:00"},
    {"date": "22.06.2025", "title": "סדנה: כלי AI לעסקים", "location": "חיפה", "time": "09:00-16:00"},
    {"date": "01.07.2025", "title": "סדנה: פיתוח יישומי AI", "location": "באר שבע", "time": "09:00-17:00"},
    {"date": "10.07.2025", "title": "הרצאה: מהפכת ה-Generative AI", "location": "ירושלים", "time": "19:00-21:00"},
]

for event in events:
    st.markdown(f"""
    <div class="workshop-card rtl-text" style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <div class="workshop-title">{event['title']}</div>
            <div class="workshop-details">
                <strong>מיקום:</strong> {event['location']}<br>
                <strong>שעה:</strong> {event['time']}
            </div>
        </div>
        <div style="text-align: center; background-color: #3B82F6; color: white; padding: 15px; border-radius: 5px; font-weight: bold; min-width: 100px;">
            {event['date']}
        </div>
    </div>
    """, unsafe_allow_html=True)

# פוטר
st.markdown("""
<div class="footer">
    <p>© כל הזכויות שמורות לשגיא בר און 2025 | מומחה בינה מלאכותית ומרצה</p>
    <p>
        <a href="#" style="margin: 0 10px; color: #3B82F6;">LinkedIn</a>
        <a href="#" style="margin: 0 10px; color: #3B82F6;">Twitter</a>
        <a href="#" style="margin: 0 10px; color: #3B82F6;">Facebook</a>
        <a href="#" style="margin: 0 10px; color: #3B82F6;">YouTube</a>
    </p>
</div>
""", unsafe_allow_html=True)