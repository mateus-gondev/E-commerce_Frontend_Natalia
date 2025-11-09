const USER_KEY = "user";

export default {
  // Salva o usuário no localStorage
    saveUser(user) {
        localStorage.setItem(USER_KEY, JSON.stringify(user));
        // Aqui eu vou ta emitindo um evento global para navbar atualizar
        window.dispatchEvent(new Event("user-login"));
    },

  // Aqui eu recupero o usuário logado
    getUser() {
        const storedUser = localStorage.getItem(USER_KEY);
        return storedUser ? JSON.parse(storedUser) : null;
    },

    // Remove o usuário do localStorage
    clearUser() {
        localStorage.removeItem(USER_KEY);
        window.dispatchEvent(new Event("user-logout"));
    },
};