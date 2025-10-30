<template>
    <div class="register-page">
        <div class="container py-5">
            <div class="row justify-content-center">
                <div class="col-lg-5 col-md-7">
                    <div class="register-card bg-white rounded shadow p-4 p-md-5">
                        <div class="text-center mb-4">
                            <i class="bi bi-gem fs-1 text-primary"></i>
                            <h2 class="fw-bold mt-3">Criar Conta</h2>
                            <p class="text-muted">Junte-se a nós hoje</p>
                        </div>

                        <form @submit.prevent="handleRegister">
                            <div class="mb-3">
                                <label for="name" class="form-label">Nome Completo</label>
                                <div class="input-group">
                                    <span class="input-group-text">
                                        <i class="bi bi-person"></i>
                                    </span>
                                    <input type="text" class="form-control" id="name" v-model="name"
                                        placeholder="Seu nome completo" required />
                                </div>
                            </div>

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
                                        placeholder="Mínimo 6 caracteres" required />
                                </div>
                            </div>

                            <div class="mb-3">
                                <label for="confirmPassword" class="form-label">Confirmar Senha</label>
                                <div class="input-group">
                                    <span class="input-group-text">
                                        <i class="bi bi-lock-fill"></i>
                                    </span>
                                    <input type="password" class="form-control" id="confirmPassword"
                                        v-model="confirmPassword" placeholder="Confirme sua senha" required />
                                </div>
                            </div>

                            <div class="mb-3 form-check">
                                <input type="checkbox" class="form-check-input" id="terms" required />
                                <label class="form-check-label small" for="terms">
                                    Concordo com os <a href="#">Termos de Uso</a> e
                                    <a href="#">Política de Privacidade</a>
                                </label>
                            </div>

                            <button type="submit" class="btn btn-primary w-100 btn-lg mb-3">
                                <i class="bi bi-person-plus me-2"></i>
                                Criar Conta
                            </button>
                        </form>

                        <hr class="my-4" />

                        <div class="text-center">
                            <p class="text-muted mb-2">Já tem uma conta?</p>
                            <router-link to="/login" class="btn btn-outline-primary w-100">
                                Fazer Login
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
    name: "Cadastro"
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
