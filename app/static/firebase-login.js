// firebase-login.js
// Must be served via: <script type="module" src="/static/firebase-login.js"></script>

// Import Firebase modules
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.4.0/firebase-app.js";
import {
  getAuth,
  signInWithEmailAndPassword,
  signOut,
  onAuthStateChanged
} from "https://www.gstatic.com/firebasejs/11.4.0/firebase-auth.js";

// ----- 1) Firebase Configuration
const firebaseConfig = {
  apiKey: "AIzaSyD1f3xPSu8nDWaPO-6r29MrDGo7e_tIfVU",
  authDomain: "f1-driver-registry.firebaseapp.com",
  projectId: "f1-driver-registry",
  storageBucket: "f1-driver-registry.appspot.com",
  messagingSenderId: "425340909294",
  appId: "1:425340909294:web:612a49c0471636a2ef65ff"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

// ----- 2) onAuthStateChanged: Toggles login panels + restricted buttons
onAuthStateChanged(auth, (user) => {
  if (user) {
    console.log("User logged in:", user.email);

    // Hide loggedOutPanel, show loggedInPanel
    const loggedOutPanel = document.getElementById("loggedOutPanel");
    if (loggedOutPanel) loggedOutPanel.style.display = "none";

    const loggedInPanel = document.getElementById("loggedInPanel");
    if (loggedInPanel) loggedInPanel.style.display = "flex";

    // Show restricted buttons
    const restrictedBtns = [
      "btn_add_driver",
      "btn_modify_driver",
      "btn_delete_driver",
      "btn_add_team",
      "btn_modify_team",
      "btn_delete_team"
    ];
    for (const btnId of restrictedBtns) {
      const btnEl = document.getElementById(btnId);
      if (btnEl) {
        btnEl.style.display = "inline-block";
      }
    }

    // Update user email label
    const userEmailLabel = document.getElementById("userEmailLabel");
    if (userEmailLabel) {
      userEmailLabel.textContent = `Logged in as: ${user.email}`;
    }

    // Retrieve ID token, store in localStorage
    user.getIdToken().then(token => {
      localStorage.setItem("idToken", token);
      console.log("ID token stored:", token.slice(0,10), "...");
    });

  } else {
    console.log("No user logged in");

    // Show loggedOutPanel, hide loggedInPanel
    const loggedOutPanel = document.getElementById("loggedOutPanel");
    if (loggedOutPanel) loggedOutPanel.style.display = "flex";

    const loggedInPanel = document.getElementById("loggedInPanel");
    if (loggedInPanel) loggedInPanel.style.display = "none";

    // Hide restricted buttons
    const restrictedBtns = [
      "btn_add_driver",
      "btn_modify_driver",
      "btn_delete_driver",
      "btn_add_team",
      "btn_modify_team",
      "btn_delete_team"
    ];
    for (const btnId of restrictedBtns) {
      const btnEl = document.getElementById(btnId);
      if (btnEl) {
        btnEl.style.display = "none";
      }
    }

    // Clear ID token
    localStorage.removeItem("idToken");
  }
});

// ----- 3) signInUser function
function signInUser() {
  // A very basic prompt-based login. You could build a real form if you prefer.
  const email = prompt("Email:");
  if (!email) return;
  const password = prompt("Password:");
  if (!password) return;

  signInWithEmailAndPassword(auth, email, password)
    .then((userCredential) => {
      console.log("Signed in as:", userCredential.user.email);
    })
    .catch((error) => {
      console.error("Sign-in error:", error);
      alert(error.message);
    });
}

// ----- 4) signOutUser function
function signOutUser() {
  signOut(auth)
    .then(() => {
      console.log("User signed out");
    })
    .catch((error) => {
      console.error("Sign-out error:", error);
    });
}

// ----- 5) Attach to window
window.showLoginDialog = signInUser;
window.signOutUser = signOutUser;
