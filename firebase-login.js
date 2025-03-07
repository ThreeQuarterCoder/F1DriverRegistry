
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

  // Track login state
  onAuthStateChanged(auth, (user) => {
    if (user) {
      console.log("User logged in:", user.email);
      // Show/hide elements for logged-in state
    } else {
      console.log("No user logged in");
      // Show/hide elements for logged-out state
    }
  });

  // Basic sign-in function
  function signInUser() {
    const email = document.getElementById("emailInput").value;
    const password = document.getElementById("passwordInput").value;

    signInWithEmailAndPassword(auth, email, password)
      .then((userCredential) => {
        console.log("Signed in as:", userCredential.user.email);
      })
      .catch((error) => {
        console.error("Sign-in error:", error);
        alert(error.message);
      });
  }

  // Basic sign-out function
  function signOutUser() {
    signOut(auth)
      .then(() => {
        console.log("User signed out");
      })
      .catch((error) => {
        console.error("Sign-out error:", error);
      });
  }

  // Attach functions to global scope for button click events
  window.signInUser = signInUser;
  window.signOutUser = signOutUser;

