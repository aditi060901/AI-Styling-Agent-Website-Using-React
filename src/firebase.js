

import { initializeApp } from "firebase/app";
import { getAuth } from 'firebase/auth';
import { getStorage } from 'firebase/storage';




const firebaseConfig = {
  apiKey: "apikey",
  authDomain: "dom",
  projectId: "id",
  storageBucket: "bkt",
  messagingSenderId: "sid",
  appId: "aid"
};


const app = initializeApp(firebaseConfig);


const auth = getAuth(app);
const storage = getStorage(app);

export { auth, storage };