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

                        <form>
                            <div class="mb-3">
                                <label for="name" class="form-label fw-semibold">Nome Completo</label>
                                <input type="text" class="form-control" id="name" placeholder="Seu nome completo"
                                    required />
                            </div>

                            <div class="mb-3">
                                <label for="email" class="form-label fw-semibold">E-mail</label>
                                <input type="email" class="form-control" id="email" placeholder="seu@email.com"
                                    required />
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
    name: "FormCadastro",
    data() {
        return {
            password: "",
            mostrarSenha: false,
        };
    },

};
</script>

<style scoped>
.register-page {
    min-height: 100vh;
    background: linear-gradient(135deg, #fff8e7 0%, #f5e1b9 100%);
    display: flex;
    align-items: center;
}

.register-card {
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
