
  // Import Firebase modules correctly
  import { initializeApp } from "https://www.gstatic.com/firebasejs/11.4.0/firebase-app.js";
  import { getAuth, signInWithEmailAndPassword, signOut, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/11.4.0/firebase-auth.js";

  // Firebase configuration
  const firebaseConfig = {
    apiKey: "AIzaSyD1f3xPSu8nDWaPO-6r29MrDGo7e_tIfVU",
    authDomain: "f1-driver-registry.firebaseapp.com",
    projectId: "f1-driver-registry",
    storageBucket: "f1-driver-registry.appspot.com",
    messagingSenderId: "425340909294",
    appId: "1:425340909294:web:612a49c0471636a2ef65ff"
  };

  // Initialize Firebase App
  const app = initializeApp(firebaseConfig);

  // Initialize Firebase Authentication
  const auth = getAuth(app);

  // ----- 2) onAuthStateChanged: Show/hide panels, store token
onAuthStateChanged(auth, (user) => {
  if (user) {
    console.log("User logged in:", user.email);
    // Show loggedInPanel, hide loggedOutPanel
    const loggedOutPanel = document.getElementById("loggedOutPanel");
    if (loggedOutPanel) {
      loggedOutPanel.style.display = "none";
    }
    const loggedInPanel = document.getElementById("loggedInPanel");
    if (loggedInPanel) {
      loggedInPanel.style.display = "flex";
    }

    // Update label
    const userEmailLabel = document.getElementById("userEmailLabel");
    if (userEmailLabel) {
      userEmailLabel.textContent = `Logged in as: ${user.email}`;
    }

    // Retrieve the ID token and store in localStorage
    user.getIdToken().then(token => {
      localStorage.setItem("idToken", token);
      console.log("ID token stored in localStorage:", token.slice(0, 10), "..."); // partial logging
    });

  } else {
    console.log("No user logged in");
    // Show loggedOutPanel, hide loggedInPanel
    const loggedOutPanel = document.getElementById("loggedOutPanel");
    if (loggedOutPanel) {
      loggedOutPanel.style.display = "flex";
    }
    const loggedInPanel = document.getElementById("loggedInPanel");
    if (loggedInPanel) {
      loggedInPanel.style.display = "none";
    }
    // Clear ID token
    localStorage.removeItem("idToken");
  }
});

// ----- 3) signInUser function -----
function signInUser() {
  // For demonstration, let's just do a quick prompt, or you can do
  // a real form from the UI
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

// ----- 4) signOutUser function -----
function signOutUser() {
  signOut(auth)
    .then(() => {
      console.log("User signed out");
    })
    .catch((error) => {
      console.error("Sign-out error:", error);
    });
}

// ----- 5) Attach to window so we can call them from Python code's on_click
window.showLoginDialog = signInUser;
window.signOutUser = signOutUser;