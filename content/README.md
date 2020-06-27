## src
  * compiler -- 编译相关
  * core -- 
  * platforms -- 平台
  * server -- 服务端渲染
  * sfc -- 解释器
  * shared -- 辅助方法

  vue 本身是一个函数,用函数来是现一个类(vue 2.x 版本),类上挂很多原型方法。
  通过 defineProperty 定义一个全局 config。
  在 import 引入 vue 的过程中定义的一些全局方法。(初始化过程，定义，Mixin 挂载原型方法)