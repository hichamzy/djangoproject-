<template>
  <div class="">
    <div class="mt-6 lg:mt-24 container mx-auto">
      <h2
        class="text-2xl md:text-3xl lg:text-4xl text-gray-800 capitalize font-bold flex justify-center"
      >
        Journal
      </h2>
      <div
        class="grid grid-cols-1 ms:grid-cols-3 md:grid-cols-3 ms:gap-x-6 md:gap-x-12 gap-y-12 w-full mt-8"
      >
        <div class="w-full" v-for="(n, index) in 3" :key="index">
          <div class="w-full h-36 md:h-44 xl:h-56 overflow-hidden">
            <img
              :src="require(`../assets/images/blog${index + 1}.png`)"
              class="object-cover rounded overflow-hidden transition-all hover:scale-125 transform duration-500 w-full h-full"
            />
          </div>
          <div class="mt-1 xl:mt-2">
            <h2
              class="text-luna-gray-300 capitalize text-base lg:text-lg xl:text-2xl font-medium lg:pr-4 xl:pr-16"
            >
              Connecting artificial intelegenet with digital product design
            </h2>
          </div>
          <div class="flex mt-4">
            <div class="mr-2">
              <img
                src="../assets/images/writer.jpeg"
                class="w-8 h-8 xl:w-8 xl:h-8 object-cover rounded-full"
                alt=""
              />
            </div>
            <div class="flex flex-col flex-1">
              <p
                class="text-luna-sm lg:text-luna-xs xl:text-xs text-luna-gray-300"
              >
                BY
                <span class="capitalize font-semibold">mika matikainen</span> is
                a Design founder @advisor, Berlin School of Creative Leadership
                Executive
              </p>
              <p
                class="capitalize text-luna-sm font-bold mt-1 lg:text-luna-xs xl:text-xs text-gray-600"
              >
                may 20th 2020
              </p>
            </div>
          </div>
        </div>
      </div>
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
