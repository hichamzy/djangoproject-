<template>
  <div class="mt-8 md:mt-12 lg:mt-16">
    <h2
      class="text-2xl md:text-3xl lg:text-4xl text-gray-800 capitalize font-bold flex justify-center"
    >
      our products
    </h2>
    <div
      class="lg:container lg:mx-auto grid grid-cols-2 ms:grid-cols-3 md:grid-cols-4 lg:grid-cols-4 gap-6 md:gap-6 lx:gap-x-8 xl:gap-8 px-5 md:px-8 lm:px-16 lx:px-16 xl:px-48 mt-6 md:mt-8 lg:mt-12"
    >
      <router-link
        to="/product"
        class="relative flex flex-col bg-gray-50"
        v-for="(n, index) in 8"
        :key="index"
      >
        <img
          :src="require(`../assets/images/image${index + 1}.png`)"
          class="w-full h-36 ms:h-44 md:h-52 lm:h-52 lg:h-64 object-cover overflow-hidden"
          alt=""
        />
        <div class="px-2 md:px-4 py-3 md:py-4">
          <h1
            class="tracking-wide text-gray-900 capitalize text-xs md:text-base xl:text-lg font-semibold"
          >
            Stylish cage chair
          </h1>
          <p class="text-luna-xs md:text-xs my-1 text-gray-400">
            Minimalist flower pot
          </p>
          <div class="flex flex-col lg:flex-row lg:items-end">
            <p class="text-gray-700 font-semibold mr-3 text-xs md:text-base">
              300.00 DH
            </p>
            <p
              class="text-gray-500 text-luna-xs md:text-sm mt-0 lg:mt-0 line-through"
            >
              400.00 DH
            </p>
          </div>
        </div>
        <div
          class="w-8 h-8 md:w-10 md:h-10 lg:w-12 lg:h-12 flex justify-center items-center absolute bg-gray-800 text-gray-100 top-2 right-2 lg:top-4 lg:right-4 rounded-full text-luna-xs md:text-xs lg:text-sm"
        >
          -30%
        </div>
      </router-link>
    </div>
    <div class="flex justify-center mt-10">
      <button
        class="px-16 py-2 text-gray-900 capitalize text-sm font-semibold border border-gray-900 hover:bg-gray-900 hover:text-gray-100 transition-colors duration-200 outline-none"
      >
        show more
      </button>
    </div>
  </div>
</template>
