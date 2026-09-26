# ES6 Promises

مشروع عن الـ Promises في JavaScript: كيف تنشئها، كيف تتعامل مع النجاح والفشل،
وكيف تنسّق عدة عمليات غير متزامنة مع بعض.

## المفاهيم

| المفهوم | الشرح |
| --- | --- |
| `new Promise((resolve, reject) => {})` | إنشاء وعد جديد: `resolve` عند النجاح، `reject` عند الفشل |
| `.then()` | ينفّذ عند نجاح الوعد |
| `.catch()` | ينفّذ عند فشل الوعد |
| `.finally()` | ينفّذ في كل الحالات |
| `Promise.resolve(v)` | وعد ناجح جاهز بالقيمة `v` |
| `Promise.reject(e)` | وعد مرفوض جاهز بالخطأ `e` |
| `Promise.all([...])` | ينتظر كل الوعود، ويفشل لو فشل واحد |
| `Promise.allSettled([...])` | ينتظر كل الوعود ويرجع حالة كل واحد بدون فشل عام |
| `Promise.race([...])` | يرجع أول وعد يخلص |
| `throw` / `try…catch…finally` | معالجة الأخطاء المتزامنة |

## الملفات

| الملف | المهمة |
| --- | --- |
| `utils.js` | دوال مساعدة: `uploadPhoto`, `createUser` |
| `0-promise.js` | يرجع Promise |
| `1-promise.js` | Promise ينجح أو يُرفض حسب `success` |
| `2-then.js` | استخدام `then` و `catch` و `finally` |
| `3-all.js` | `Promise.all` مع دالتين |
| `4-user-promise.js` | `Promise.resolve` لكائن مستخدم |
| `5-photo-reject.js` | `Promise.reject` مع رسالة خطأ |
| `6-final-user.js` | `Promise.allSettled` وتجميع النتائج |
| `7-load_balancer.js` | `Promise.race` لاختيار الأسرع |
| `8-try.js` | `throw` عند القسمة على صفر |
| `9-try.js` | `try…catch…finally` وبناء قائمة النتائج |

## التشغيل

```bash
npm install
npm run dev 0-main.js
npm run full-test
```
