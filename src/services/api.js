import axios from "axios";

const api = axios.create({
  baseURL: "http://10.100.0.158:5000/api", // ajuste para IP correto do backend
  headers: {
    "Content-Type": "application/json",
  },
});

export default api;
