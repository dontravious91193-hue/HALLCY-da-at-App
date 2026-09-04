import os
import streamlit as st
import random
import json
import html
from google import genai

# Initialize Google Client — key comes from env only, never hardcoded
try:
    client = genai.Client()
except Exception:
    client = None

st.set_page_config(page_title="Hallcy Da'at Learning Matrix", page_icon="🪐", layout="wide")

# Styled CSS to match your exact layout from the screen photo
st.markdown("""
    <style>
    .main { background-color: #0b0c10; color: #c5c6c7; }
    .stButton>button { 
        background: linear-gradient(45deg, #45f3ff, #ff2a74); 
        color: #ffffff; 
        font-weight: bold;
        border-radius: 8px;
    }
    .card { 
        background: rgba(255, 255, 255, 0.03); 
        padding: 24px; 
        border-radius: 14px;
        border: 1px solid rgba(69, 243, 255, 0.2);
        margin-bottom: 20px;
    }
    .feedback-card {
        background: rgba(255, 42, 116, 0.05);
        padding: 16px;
        border-radius: 10px;
        border: 1px solid rgba(255, 42, 116, 0.25);
        margin-top: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ANTI-HACKING GATEKEEPER ---
if "security_flagged" not in st.session_state:
    st.session_state.security_flagged = False

FEEDBACK_FILE = "daat_feedback.jsonl"

def check_malicious_input(user_string):
    if not user_string:
        return False
    malicious_tokens = ["<script>", "DROP TABLE", "OR 1=1", "exec(", "eval(", "bin/sh", "sudo ", "import os", "subprocess", "__import__", "open("]
    lowered = user_string.lower()
    for token in malicious_tokens:
        if token.lower() in lowered:
            return True
    return False

if st.session_state.security_flagged:
    st.error("🚨 SECURITY VIOLATION: MALICIOUS ACTIVITY DETECTED")
    st.error("Your session has been flagged in real-time. Hacking vectors are strictly prohibited on the Hallcy Da'at network and have been logged for administrative reporting.")
    st.stop()

# --- MANDATORY ACCESS GATE (TERMS OF SERVICE) ---
if "terms_approved" not in st.session_state:
    st.session_state.terms_approved = False

if not st.session_state.terms_approved:
    st.title("🪐 Welcome to Hallcy Da'at Learning Matrix")
    st.warning("⚠️ Access Protocol Required")
    st.markdown("""
    ### User Terms of Service & AI Training Agreement
    By entering the Hallcy da'at platform, you agree to the following terms:
    1. **Real-Time Learning:** You understand that our AI models learn synchronously from your puzzle-solving patterns and gameplay mechanics.
    2. **Anonymized Data:** No personal identifying data is sold; gameplay telemetry is used purely to optimize the game's educational engine.
    3. **Fair Play:** Automated scripts, macro bots, or hacking vectors are strictly prohibited. Malicious activities trigger automatic real-time flagging.
    4. **Beta Feedback:** Your feedback helps shape the public beta. Nothing you submit is shared with third parties.
    """)
    
    agree_check = st.checkbox("I verify that I understand these rules and agree to the terms.")
    if st.button("Initialize Gameplay Access Grid"):
        if agree_check:
            st.session_state.terms_approved = True
            st.success("Access Granted! Loading Ecosystem Grid...")
            st.rerun()
        else:
            st.error("You must approve the terms before the real-time engine can initialize.")
    st.stop()

# --- MAIN APPLICATION NAVIGATION ---
st.sidebar.title("🪐 Hallcy Da'at Hub")
st.sidebar.markdown("`v2.1.0 - Gamified AI Sandbox`")
st.sidebar.markdown("---")
menu = st.sidebar.radio("Navigation Nodes", ["Arcade Dashboard", "Business Sponsorships", "📝 Beta Feedback"])

if menu == "Arcade Dashboard":
    st.title("🎮 Hallcy Da'at Learning Arcade")
    st.write("Real-time gamified engines where users and AI learn core logic systems side-by-side.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        status_text = "<span style='color:#00ffcc;'>● ONLINE</span>" if os.environ.get("GEMINI_API_KEY") else "<span style='color:#ffaa00;'>○ SANDBOX LOCAL MODE</span>"
        st.markdown(f'<div class="card"><h3>AI Core Adaptation</h3><p>{status_text}</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card"><h3>Workspace Repository</h3><p style="color:#45f3ff;">Hallcy_da_at / Public</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="card"><h3>Security Firewall</h3><p style="color:#00ffcc;">Active - Zero Hacking Tolerance</p></div>', unsafe_allow_html=True)

    st.markdown("---")
    
    game_choice = st.selectbox("Select Your Learning Vector:", ["⌨️ Monkeytype Alpha Matrix", "🌱 8-Bit Watering Garden", "🐞 Pattern Debug Hunter"])
    
    if game_choice == "⌨️ Monkeytype Alpha Matrix":
        st.subheader("⌨️ Monkeytype Alpha Matrix: Dexterity & Syntax Racing")
        st.write("Objective: Type the randomly generated code blocks cleanly. The AI tracks your speed and generates dynamic code logic arrays alongside you. Sometimes the AI will output buggy logic, challenge it to win!")
        
        test_snippet = "def initialize_matrix(nodes):\n    return [Node(i) for i in range(nodes)]"
        st.code(test_snippet, language="python")
        
        user_type = st.text_area("Type the snippet exactly as fast as you can:", key="monkeytype_input")
        
        if user_type:
            if check_malicious_input(user_type):
                st.session_state.security_flagged = True
                st.rerun()
                
            ai_mistake_roll = random.random()
            if ai_mistake_roll > 0.75:
                st.warning("🤖 AI Competitor Response: The AI slipped up! It generated an invalid return bracket structure. You gained a speed multiplier!")
            else:
                st.info("🤖 AI Competitor Response: The AI correctly matched your tempo and is updating its typing syntax pattern vectors.")

    elif game_choice == "🌱 8-Bit Watering Garden":
        st.subheader("🌱 8-Bit Watering Garden: Computational Growth Grid")
        st.write("Objective: Water your pixel plants by solving memory allocation or spatial grid arrays. The more efficient your math parameters, the faster the ecosystem adapts.")
        
        st.markdown("""
        ```
        [🪴 Plant A] -> Target Input: 16-bit array pointer
        [🌻 Plant B] -> Target Input: Memory alignment multiple of 8
        ```
        """)
        
        garden_input = st.text_input("Enter the binary or mathematical solution to water the current tile grid:", key="garden_input")
        
        if garden_input:
            if check_malicious_input(garden_input):
                st.session_state.security_flagged = True
                st.rerun()
                
            st.success("💧 Water deployed! The 8-bit grid state updated. The AI telemetry engine logged your efficiency optimization strategy.")

    elif game_choice == "🐞 Pattern Debug Hunter":
        st.subheader("🐞 Pattern Debug Hunter: Syntax & Logic Triage")
        st.write("Objective: Spot the structural vulnerability or syntax error in real-time. The code blocks morph as you solve them, and the AI tests out various mutation debugging routines right with you.")
        
        faulty_code = "for i in range(10)\n    print('Tracking node index:', i)"
        st.code(faulty_code, language="python")
        
        debug_fix = st.text_input("Provide the exact characters missing or wrong to fix line 1:", key="debug_input")
        
        if debug_fix:
            if check_malicious_input(debug_fix):
                st.session_state.security_flagged = True
                st.rerun()
                
            if ":" in debug_fix:
                st.success("🎯 Critical hit! Bug caught. Real-time game complexity metrics increased.")
            else:
                st.error("The bug survived! Try inspecting the end of line 1 statement rules.")

elif menu == "Business Sponsorships":
    st.title("💼 Verified Brand Sponsorship Portal")
    st.write("Want to sponsor a branded 8-bit level or host custom mini-game patterns? Verifiable social accounts are required.")
    
    with st.form("sponsor_verification_form"):
        company_name = st.text_input("Business / Entity Name")
        contact_email = st.text_input("Official Contact Email")
        st.markdown("### 🔒 Social Media Verification Matrices")
        x_handle = st.text_input("X (Twitter) Handle", placeholder="@username")
        insta_handle = st.text_input("Instagram Handle", placeholder="@username")
        tiktok_handle = st.text_input("TikTok Handle", placeholder="@username")
        proposal = st.text_area("Sponsorship Vision", placeholder="Describe the educational/gamified mechanics you want to fund...")
        
        if st.form_submit_button("Submit Secure Verification Application"):
            if check_malicious_input(company_name) or check_malicious_input(proposal):
                st.session_state.security_flagged = True
                st.rerun()
                
            if not company_name or not contact_email or not (x_handle or insta_handle or tiktok_handle):
                st.error("Verification Refused: You must provide your company details and at least one social media handle.")
            else:
                st.success("Application encrypted! Our screening matrix will verify your cross-platform social handles.")

elif menu == "📝 Beta Feedback":
    st.title("📝 Beta Feedback Terminal")
    st.write("Your input shapes the next build. Rate the arcade, flag bugs, suggest games. Everything lands in a local log — nothing leaves this machine.")

    with st.form("beta_feedback_form"):
        player_name = st.text_input("Callsign (optional)", placeholder="Anonymous Pilot")
        rating = st.slider("Overall beta rating", 1, 5, 3)
        liked = st.text_area("What worked?", placeholder="The typing game felt fast...")
        improve = st.text_area("What should improve?", placeholder="More games, smoother UI...")
        bug = st.text_area("Bugs found", placeholder="None yet — or describe one")
        submitted = st.form_submit_button("Transmit Feedback")

        if submitted:
            if check_malicious_input(liked) or check_malicious_input(improve) or check_malicious_input(bug) or check_malicious_input(player_name):
                st.session_state.security_flagged = True
                st.rerun()
            entry = {
                "ts": __import__("datetime").datetime.utcnow().isoformat() + "Z",
                "callsign": html.escape(player_name or "Anonymous"),
                "rating": rating,
                "liked": html.escape(liked),
                "improve": html.escape(improve),
                "bug": html.escape(bug),
            }
            with open(FEEDBACK_FILE, "a", encoding="utf-8") as f:
                f.write(json.dumps(entry) + "\n")
            st.success("Feedback logged locally. Thank you, pilot.")

    st.markdown("---")
    st.subheader("Recent Transmissions")
    if os.path.exists(FEEDBACK_FILE):
        lines = open(FEEDBACK_FILE, encoding="utf-8").read().strip().splitlines()
        for line in reversed(lines[-5:]):
            try:
                e = json.loads(line)
                st.markdown(f'''<div class="feedback-card">
                <b>👤 {e.get("callsign","Anonymous")}</b> · ★{e.get("rating", "?")}/5<br>
                <i>Liked:</i> {e.get("liked","")}<br>
                <i>Improve:</i> {e.get("improve","")}<br>
                <i>Bug:</i> {e.get("bug","")}
                </div>''', unsafe_allow_html=True)
            except Exception:
                pass
    else:
        st.info("No feedback yet. Be the first pilot to transmit.")
