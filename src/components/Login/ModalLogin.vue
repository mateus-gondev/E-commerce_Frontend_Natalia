<template>
    <transition name="slide-login">
        <div v-if="loginAberto" class="login-slider bg-white shadow position-fixed"
            style="top: 0; right: 0; height: 100vh; width: 350px; z-index: 1100;">
            <div class="d-flex justify-content-between align-items-center p-3 border-bottom">
                <h5 class="mb-0">
                    <i class="fas fa-gem me-2 text-warning"></i> Menu
                </h5>
                <button class="btn-close-custom" @click="fecharMenu" title="Fechar">
                    &times;
                </button>
            </div>

            <div class="p-4 text-center text-muted d-flex flex-column justify-content-center"
                style="height: calc(100vh - 120px);">
                <i class="fas fa-user-cijrcle fa-4x mb-4 text-warning"></i>
                <p class="fw-semibold text-dark">Realize seu login</p>

                <button class="btn-login-entrar" @click="irParaLogin">
                    Entrar
                </button>


            </div>
        </div>
    </transition>
</template>

<script>
export default {
    name: "ModalLogin",
    data() {
        return {
            loginAberto: false,
        };
    },
    methods: {
        abrirMenu() {
            this.loginAberto = true;
        },
        fecharMenu() {
            this.loginAberto = false;
        },
        irParaLogin() {
            this.fecharMenu();
            setTimeout(() => {
                this.$router.push('/login');
            }, 400); // espera o slide fechar
        },
    },
};
</script>

<style scoped>
.slide-login-enter-active,
.slide-login-leave-active {
    transition: transform 0.4s ease;
}

.slide-login-enter-from,
.slide-login-leave-to {
    transform: translateX(100%);
}

.slide-login-enter-to,
.slide-login-leave-from {
    transform: translateX(0);
}

.btn-close-custom {
    background: none;
    border: none;
    font-size: 1.8rem;
    color: #777;
    cursor: pointer;
    transition: color 0.3s ease;
}

.btn-close-custom:hover {
    color: #000;
}

.btn-login-entrar {
    display: inline-block;
    padding: 10px 28px;
    border-radius: 25px;
    font-weight: 600;
    background: linear-gradient(135deg, #d4af37, #f8e08e);
    color: #fff;
    text-decoration: none;
    transition: all 0.3s ease;
    box-shadow: 0 4px 10px rgba(212, 175, 55, 0.3);
}

.btn-login-entrar:hover {
    background: linear-gradient(135deg, #b8952e, #f6d86d);
    box-shadow: 0 6px 14px rgba(212, 175, 55, 0.5);
    transform: translateY(-2px);
    color: #fff;
}
</style>