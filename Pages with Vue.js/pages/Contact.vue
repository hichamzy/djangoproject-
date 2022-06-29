<template>
  <div class="container mx-auto mt-24 lg:px-40 lx:px-52 xl:px-80">
    <h1 class="text-4xl text-center">Contact</h1>
    <div class="mt-12 md:mt-16 text-luna-gray-300">
      <p class="text-sm md:text-base font-semibold">Have a Question?</p>
      <div class="mt-4">
        <img
          src="../assets/images/contact.png"
          class="w-full h-72 object-cover"
          alt=""
        />
      </div>
      <p class="text-xs font-semibold mt-2">
        we're here to help answer any question you have
      </p>
      <div class="mt-8">
        <div class="grid md:grid-cols-2 gap-y-5 gap-x-12">
          <div class="flex flex-col">
            <label for="name" class="text-luna-sm font-semibold"
              >Name <span class="text-red-300">*</span></label
            >
            <input
              class="mt-1 w-full border bg-white py-2 px-2 text-xs text-luna-gray-300 outline-none rounded"
              type="text"
              id="name"
            />
          </div>
          <div class="flex flex-col">
            <label for="name" class="text-luna-sm font-semibold"
              >Name <span class="text-red-300">*</span></label
            >
            <input
              class="mt-1 w-full border bg-white py-2 px-2 text-xs text-luna-gray-300 outline-none rounded"
              type="text"
              id="name"
            />
          </div>
        </div>
        <div class="mt-5">
          <div class="flex flex-col">
            <label for="email" class="text-luna-sm font-semibold"
              >Email <span class="text-red-300">*</span></label
            >
            <input
              class="mt-1 w-full border bg-white py-2 px-2 text-xs text-luna-gray-300 outline-none rounded"
              type="email"
              id="email"
            />
          </div>
        </div>
        <div class="mt-5">
          <div class="flex flex-col">
            <label for="message" class="text-luna-sm font-semibold"
              >Message <span class="text-red-300">*</span></label
            >
            <textarea
              class="mt-1 w-full border bg-white py-2 px-2 text-xs text-luna-gray-300 outline-none rounded resize-none"
              rows="10"
              type="email"
              id="email"
            />
          </div>
        </div>
        <div class="mt-5">
          <button
            class="border border-gray-900 hover:bg-transparent bg-gray-900 hover:text-gray-900 font-semibold transition-all duration-200 outline-none focus:outline-none text-white px-10 py-2 text-xs"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
