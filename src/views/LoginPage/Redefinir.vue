<template>
    <div class="reset-page">
        <div class="container py-5">
            <div class="row justify-content-center">
                <div class="col-lg-5 col-md-7">
                    <div class="reset-card bg-white rounded shadow p-4 p-md-5">
                        <div class="text-center mb-4">
                            <i class="bi bi-gem fs-1 text-gold"></i>
                            <h2 class="fw-bold mt-3 text-dark">Redefinir Senha</h2>
                            <p class="text-muted">
                                Insira seu e-mail para receber o link de redefinição de senha
                            </p>
                        </div>

                        <form @submit.prevent="enviarEmail">
                            <div class="mb-4">
                                <label for="email" class="form-label fw-semibold">E-mail</label>
                                <div class="input-group">
                                    <span class="input-group-text bg-light">
                                        <i class="bi bi-envelope text-gold"></i>
                                    </span>
                                    <input type="email" class="form-control" id="email" v-model="email"
                                        placeholder="seu@email.com" required />
                                </div>
                            </div>

                            <button type="submit" class="btn btn-gold w-100 btn-lg mb-3">
                                <i class="bi bi-send me-2"></i>
                                Enviar Link de Redefinição
                            </button>
                        </form>

                        <hr class="my-4" />

                        <div class="text-center">
                            <router-link to="/login" class="btn btn-outline-gold w-100 mb-3">
                                <i class="bi bi-box-arrow-in-right me-2"></i> Voltar ao Login
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
    name: "Redefinir",
    data() {
        return {
            email: "",
        };
    },
    methods: {
        enviarEmail() {
            alert(`Um link de redefinição foi enviado para ${this.email}`);
            this.email = "";
        },
    },
};
</script>

<style scoped>
.reset-page {
    min-height: 100vh;
    background: linear-gradient(135deg, #fff8e7 0%, #f5e1b9 100%);
    display: flex;
    align-items: center;
}

.reset-card {
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

.form-control {
    border-left: none;
}

.input-group-text {
    border-right: none;
}

.form-control:focus {
    box-shadow: none;
    border-color: #c1a25f;
}

.input-group:focus-within .input-group-text {
    border-color: #c1a25f;
    color: #c1a25f;
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
