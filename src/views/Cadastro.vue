<template>
    <div class="register-page">
        <div class="container py-5">
            <div class="row justify-content-center">
                <div class="col-lg-5 col-md-7">
                    <div class="register-card bg-white rounded shadow p-4 p-md-5">
                        <div class="text-center mb-4">
                            <i class="bi bi-gem fs-1 text-gold"></i>
                            <h2 class="fw-bold mt-3 text-dark">Criar Conta</h2>
                            <p class="text-muted">Junte-se a nós hoje</p>
                        </div>

                        <form @submit.prevent="submitRegister">
                            <div class="mb-3">
                            <label for="name" class="form-label fw-semibold">Nome Completo</label>
                            <input
                                type="text"
                                class="form-control"
                                id="name"
                                v-model="name"
                                placeholder="Seu nome completo"
                                required
                            />
                            </div>

                            <div class="mb-3">
                            <label for="email" class="form-label fw-semibold">E-mail</label>
                            <input
                                type="email"
                                class="form-control"
                                id="email"
                                v-model="email"
                                placeholder="seu@email.com"
                                required
                            />
                            </div>

                            <div class="mb-3 position-relative">
                                <label for="password" class="form-label fw-semibold">Senha</label>
                                <div class="input-group">
                                    <input :type="mostrarSenha ? 'text' : 'password'" class="form-control" id="password"
                                        placeholder="Mínimo 6 caracteres" v-model="password" required />
                                    <span class="input-group-text bg-light toggle-password"
                                        @click="mostrarSenha = !mostrarSenha">
                                        <i
                                            :class="mostrarSenha ? 'bi bi-eye-slash text-gold' : 'bi bi-eye text-gold'"></i>
                                    </span>
                                </div>
                            </div>

                            <button type="submit" class="btn btn-gold w-100 btn-lg mb-3">
                                <i class="bi bi-person-plus me-2"></i>
                                Criar Conta
                            </button>
                        </form>

                        <hr class="my-4" />

                        <div class="text-center">
                            <p class="text-muted mb-2">Já tem uma conta?</p>
                            <router-link to="/login" class="btn btn-outline-gold w-100 mb-3">
                                Fazer Login
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

export default {
    name: "Cadastro",
    data() {
        return {
            name: "",
            email: "",
            password: "",
            confirmPassword: "",
        };
    },
};
</script>


<style scoped>
.register-page {
    padding-top: 72px;
    min-height: 100vh;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    display: flex;
    align-items: center;
}

.register-card {
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
