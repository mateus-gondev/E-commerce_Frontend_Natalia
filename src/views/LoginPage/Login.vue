<template>
    <div class="login-page">
        <div class="container py-5">
            <div class="row justify-content-center">
                <div class="col-lg-5 col-md-7">
                    <div class="login-card bg-white rounded shadow p-4 p-md-5">
                        <div class="text-center mb-4">
                            <i class="bi bi-gem fs-1 text-gold"></i>
                            <h2 class="fw-bold mt-3 text-dark">Bem-vindo de volta</h2>
                            <p class="text-muted">Entre com sua conta</p>
                        </div>

                        <form>
                            <div class="mb-3">
                                <label for="email" class="form-label fw-semibold">E-mail</label>
                                <input v-model="email" type="email" class="form-control" id="email" placeholder="name@example.com" />
                            </div>

                            <div class="mb-3 position-relative">
                                <label for="password" class="form-label fw-semibold">Senha</label>
                                <div class="input-group">
                                    <input :type="mostrarSenha ? 'text' : 'password'" class="form-control" id="password"
                                        placeholder="********" v-model="password" />
                                    <span class="input-group-text bg-light toggle-password"
                                        @click="mostrarSenha = !mostrarSenha">
                                        <i
                                            :class="mostrarSenha ? 'bi bi-eye-slash text-gold' : 'bi bi-eye text-gold'"></i>
                                    </span>
                                </div>
                            </div>


                            <button @click="submitLogin" type="submit" class="btn btn-gold w-100 btn-lg mb-3">
                                <i class="bi bi-box-arrow-in-right me-2"></i>
                                Entrar
                            </button>

                            <div class="text-center">
                                <router-link to="/redefinir" class="text-decoration-none text-gold">
                                    Esqueceu sua senha?
                                </router-link>
                            </div>
                        </form>

                        <hr class="my-4" />

                        <div class="text-center">
                            <p class="text-muted mb-2">Não tem uma conta?</p>
                            <router-link to="/cadastro" class="btn btn-outline-gold w-100 mb-3">
                                Criar Conta
                            </router-link>

                            <router-link to="/" class="btn btn-light w-100 border">
                                <i class="bi bi-arrow-left me-2"></i> Voltar à loja
                            </router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import api from "@/services/api";
import storage from "@/services/storage";

export default {
    name: "Login",
    data() {
        return {
            email: "",
            password: "",
            mostrarSenha: false,
        };
    },
    methods: {
        async submitLogin(e) {
        e.preventDefault(); //Evita pg carregar
        try {
            const res = await api.post("/login", {
            email: this.email,
            password: this.password,
            });

            const user = res.data.user;
            storage.saveUser(user); // usa o serviço aqui!!

            alert("✅ Login realizado com sucesso!");
            this.$router.push("/");
        } catch (err) {
            alert(err.response?.data?.error || "❌ Credenciais inválidas");
        }
        },
    },
};
</script>

<style scoped>
.login-page {
    min-height: 100vh;
    background: linear-gradient(135deg, #fff8e7 0%, #f5e1b9 100%);
    display: flex;
    align-items: center;
}

.login-card {
    animation: fadeInUp 0.6s ease;
    border: 1px solid #eee;
}

.text-gold {
    color: #c1a25f !important;
}

.btn-gold {
    background-color: #c1a25f;
    border: none;
    color: white;
    font-weight: 500;
}

.btn-gold:hover {
    background-color: #ad8d4b;
}

.btn-outline-gold {
    border: 1px solid #c1a25f;
    color: #c1a25f;
    font-weight: 500;
}

.btn-outline-gold:hover {
    background-color: #c1a25f;
    color: white;
}
.toggle-password {
    cursor: pointer;
    border-left: none;
}

.toggle-password:hover {
    background-color: #fff8e7;
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

</style>
