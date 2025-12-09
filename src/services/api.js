import axios from "axios";

const api = axios.create({
    baseURL: "http://10.100.0.158:5000/api", // Aqui coloca o ip damaquina que ta rodando
    headers: {
        "Content-Type": "application/json",
    },
});

export default api;

