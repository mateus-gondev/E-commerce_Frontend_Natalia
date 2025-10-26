<template>
    <div class="login-page">
        <div class="container py-5">
            <div class="row justify-content-center">
                <div class="col-lg-5 col-md-7">
                    <div class="login-card bg-white rounded shadow p-4 p-md-5">
                        <div class="text-center mb-4">
                            <i class="bi bi-gem fs-1 text-primary"></i>
                            <h2 class="fw-bold mt-3">Bem-vindo de volta</h2>
                            <p class="text-muted">Entre com sua conta</p>
                        </div>

                        <form @submit.prevent="handleLogin">
                            <div class="mb-3">
                                <label for="email" class="form-label">E-mail</label>
                                <div class="input-group">
                                    <span class="input-group-text">
                                        <i class="bi bi-envelope"></i>
                                    </span>
                                    <input type="email" class="form-control" id="email" v-model="email"
                                        placeholder="seu@email.com" required />
                                </div>
                            </div>

                            <div class="mb-3">
                                <label for="password" class="form-label">Senha</label>
                                <div class="input-group">
                                    <span class="input-group-text">
                                        <i class="bi bi-lock"></i>
                                    </span>
                                    <input type="password" class="form-control" id="password" v-model="password"
                                        placeholder="Sua senha" required />
                                </div>
                            </div>

                            <div class="mb-3 form-check">
                                <input type="checkbox" class="form-check-input" id="remember" />
                                <label class="form-check-label" for="remember">
                                    Lembrar de mim
                                </label>
                            </div>

                            <button type="submit" class="btn btn-primary w-100 btn-lg mb-3">
                                <i class="bi bi-box-arrow-in-right me-2"></i>
                                Entrar
                            </button>

                            <div class="text-center">
                                <a href="#" class="text-decoration-none">Esqueceu sua senha?</a>
                            </div>
                        </form>

                        <hr class="my-4" />

                        <div class="text-center">
                            <p class="text-muted mb-2">Não tem uma conta?</p>
                            <router-link to="/register" class="btn btn-outline-primary w-100">
                                Criar Conta
                            </router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { ref } from "vue";
import { useRouter } from "vue-router";

export default {
    name: "Login",
    setup() {
        const router = useRouter();
        const email = ref("");
        const password = ref("");

        const handleLogin = () => {
            console.log("Login:", { email: email.value, password: password.value });
            router.push("/");
        };

        return { email, password, handleLogin };
    },
};
</script>


<style scoped>
.login-page {
    padding-top: 72px;
    min-height: 100vh;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    display: flex;
    align-items: center;
}

.login-card {
    animation: fadeInUp 0.5s ease;
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.input-group-text {
    background: #f8f9fa;
    border-right: none;
}

.form-control {
    border-left: none;
}

.form-control:focus {
    box-shadow: none;
    border-color: #ced4da;
}

.input-group:focus-within .input-group-text {
    border-color: #0d6efd;
    color: #0d6efd;
}

.input-group:focus-within .form-control {
    border-color: #0d6efd;
}
</style>
