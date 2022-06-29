<template>
  <div class="relative">
    <div id="luna-nav">
      <div class="bg-white" v-if="search">
        <div class="flex items-center px-6">
          <input
            type="text"
            class="w-full h-16 outline-none text-luna-gray-300"
            placeholder="Search our store"
          />
          <svg
            @click="activateSearch"
            width="24"
            height="24"
            xmlns="http://www.w3.org/2000/svg"
            fill-rule="evenodd"
            clip-rule="evenodd"
          >
            <path
              d="M12 11.293l10.293-10.293.707.707-10.293 10.293 10.293 10.293-.707.707-10.293-10.293-10.293 10.293-.707-.707 10.293-10.293-10.293-10.293.707-.707 10.293 10.293z"
            />
          </svg>
        </div>
        <hr />
      </div>
      <div class="py-5 flex justify-between items-center container mx-auto">
        <h1 class="text-xl md:text-3xl uppercase tracking-widest m-0 p-0">
          <router-link to="/"> luna </router-link>
        </h1>
        <ul
          class="lg:text-xs xl:text-sm uppercase tracking-wider hidden lg:flex"
        >
          <li class="li-hover mr-12"><router-link to="/">home</router-link></li>
          <li class="li-hover mr-12">
            <router-link to="/products">shop</router-link>
          </li>
          <li class="li-hover mr-12">
            <router-link to="/about">about</router-link>
          </li>
          <li class="li-hover mr-12">
            <router-link to="/blogs">blog</router-link>
          </li>

          <li class="li-hover">
            <router-link to="/contact">contact</router-link>
          </li>
        </ul>

        <ul class="flex items-center">
          <li class="mr-6" @click="activateSearch">
            <img
              src="../assets/images/search.png"
              class="w-5 h-5 md:w-6 md:h-6"
              alt=""
            />
          </li>
          <li class="relative mr-6">
            <img
              src="../assets/images/heart.png"
              class="w-5 h-5 md:w-6 md:h-6"
              alt=""
            />
          </li>
          <li class="mr-6">
            <div class="relative">
              <div class="relative" @click="show = !show">
                <img
                  src="../assets/images/cart.png"
                  class="w-5 h-5 md:w-6 md:h-6 cursor-pointer"
                  alt=""
                />
                <div
                  class="absolute -top-2 -right-2 w-5 h-5 rounded-full bg-luna-gray-300 text-luna-xs text-gray-100 flex justify-center items-center font-semibold"
                >
                  <p class="">11</p>
                </div>
              </div>
              <CartDown v-if="show" />
            </div>
          </li>
          <li class="mr-6">
            <router-link to="/login">
              <img
                src="../assets/images/user.png"
                class="w-5 h-5 md:w-6 md:h-6"
                alt=""
              />
            </router-link>
          </li>
          <li @click="dropDown = !dropDown" class="block md:hidden">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="18"
              height="18"
              viewBox="0 0 24 24"
              class="fill-current text-luna-gray-300"
            >
              <path d="M24 6h-24v-4h24v4zm0 4h-24v4h24v-4zm0 8h-24v4h24v-4z" />
            </svg>
          </li>
        </ul>
      </div>
      <div
        class="absolute bg-white w-full pb-4 -mt-6 shadow-lg z-50"
        v-if="dropDown"
      >
        <div class="container mx-auto">
          <ul
            class="text-sm uppercase text-luna-gray-300 tracking-wide flex flex-col last"
          >
            <li class="mr-12 mt-2"><router-link to="/">home</router-link></li>
            <li class="mr-12 mt-2">
              <router-link to="/products">products</router-link>
            </li>
            <li class="mt-2">
              <router-link to="/products">contact</router-link>
            </li>
            <li class="mt-2">
              <router-link to="/about">about</router-link>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import CartDown from "./CartDown";
export default {
  components: {
    CartDown,
  },
  data() {
    return {
      show: false,
      dropDown: false,
      search: false,
    };
  },
  mounted() {
    window.addEventListener("scroll", this.scrollPostion);
  },
  methods: {
    activateSearch() {
      this.search = !this.search;
      const nav = document.getElementById("luna-nav");
      if (this.search) {
        nav.classList.add("sticky-postion");
        nav.classList.remove("absolute-postion");
      } else {
        nav.classList.remove("sticky-postion");
        nav.classList.add("absolute-postion");
      }
    },
    scrollPostion() {
      const nav = document.getElementById("luna-nav");
      if (window.scrollY > 50) {
        nav.classList.add("sticky-postion");
        nav.classList.remove("absolute-postion");
      } else {
        nav.classList.remove("sticky-postion");
        nav.classList.add("absolute-postion");
      }
    },
  },
};
</script>
<style lang="scss" scoped>
.li-hover::after {
  content: "";
  display: block;
  width: 0;
  height: 2px;
  background: #363a41;
  transition: width 0.4s;
}

.li-hover:hover::after {
  top: 100px;
  width: 100%;
}
.absolute-postion {
  @apply absolute w-full top-0 z-40;
  h1 {
    @apply text-gray-100;
  }
  ul {
    @apply text-gray-100;
    li {
      @apply hover:bg-black hover:text-gray-100 px-2 py-1 transition-colors duration-200;
    }
  }
}
.sticky-postion {
  @apply fixed w-full top-0 z-50 bg-white shadow-xl;
  h1 {
    @apply text-luna-gray-300;
  }
  ul {
    @apply text-luna-gray-300;
  }
  li {
    @apply px-2 py-1;
  }
}
</style>
