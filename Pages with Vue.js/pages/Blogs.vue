<template>
  <div class="container mx-auto mt-24 lg:px-40 lx:px-52 xl:px-80">
    <div class="flex flex-col items-center">
      <div>
        <img
          src="../assets/images/blog.png"
          class="h-40 sm:h-52 md:h-72 lg:h-96 xl:h-120 w-full object-cover"
          alt=""
        />
      </div>
      <div class="mt-12">
        <h1 class="text-4xl font-semibold text-luna-gray-300 text-center">
          Our Blog
        </h1>
        <p class="mt-8 text-center text-luna-gray-300 text-base">know more</p>
      </div>
    </div>
    <div class="flex justify-center mt-6">
      <hr class="w-140" />
    </div>
    <div class="mt-12">
      <h2 class="text-3xl font-semibold text-gray-800 text-center">Articles</h2>
      <div class="flex justify-center mt-12">
        <div
          class="grid grid-cols-1 ms:grid-cols-2 md:grid-cols-2 gap-x-12 gap-y-16"
        >
          <router-link
            to="/blog"
            class="w-full"
            v-for="(n, index) in 8"
            :key="index"
          >
            <div class="w-full h-36 md:h-44 xl:h-56 overflow-hidden">
              <img
                :src="require(`../assets/images/blog${index + 1}.png`)"
                class="object-cover rounded overflow-hidden transition-all hover:scale-125 transform duration-500 w-full h-full"
              />
            </div>
            <div class="mt-1 xl:mt-2">
              <h2
                class="text-luna-gray-300 capitalize text-base lg:text-lg xl:text-2xl font-medium lg:pr-4 xl:pr-8"
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
                  <span class="capitalize font-semibold">mika matikainen</span>
                  is a Design founder @advisor, Berlin School of Creative
                  Leadership Executive
                </p>
                <p
                  class="capitalize text-luna-sm font-bold mt-1 lg:text-luna-xs xl:text-xs text-gray-600"
                >
                  may 20th 2020
                </p>
              </div>
            </div>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>
