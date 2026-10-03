# NodeJS Basics

مشروع عن أساسيات NodeJS: تشغيل JavaScript خارج المتصفح، قراءة الملفات،
الوصول لوسائط سطر الأوامر، وبناء سيرفرات HTTP بـ `http` و Express.

## أهداف التعلم

- تشغيل JavaScript باستخدام NodeJS
- استخدام وحدات (modules) NodeJS
- قراءة الملفات بوحدة `fs` (متزامن وغير متزامن)
- استخدام `process` للوصول لوسائط سطر الأوامر و STDIN
- بناء سيرفر HTTP صغير بوحدة `http`
- بناء سيرفر HTTP بـ Express ومسارات متقدمة
- استخدام ES6 مع `babel-node`، والتطوير السريع بـ `nodemon`

## المفاهيم

| المفهوم | الشرح |
| --- | --- |
| `module.exports` | تصدير دالة أو كلاس حتى يستوردها ملف ثاني بـ `require` |
| `process.argv` | مصفوفة وسائط سطر الأوامر؛ `argv[2]` أول وسيط من المستخدم |
| `process.stdin` | قراءة ما يكتبه المستخدم؛ حدث `readable` للقراءة و `end` للإغلاق |
| `fs.readFileSync` | قراءة متزامنة — توقف البرنامج لحين انتهاء القراءة |
| `fs.readFile` | قراءة غير متزامنة بـ callback — لا توقف الـ thread |
| `http.createServer` | سيرفر HTTP خام؛ `writeHead` للترويسات و `end` للمحتوى |
| `express()` | إطار يبسّط المسارات: `app.get(path, handler)` |
| `:major` | معامل مسار في Express، يُقرأ من `request.params` |
| `express.Router()` | فصل المسارات في ملف مستقل وربطه بـ `app.use` |

## الملفات

| الملف | المهمة |
| --- | --- |
| `database.csv` | قاعدة بيانات الطلاب المزوّدة |
| `0-console.js` | `displayMessage` تطبع نص في STDOUT |
| `1-stdin.js` | قراءة اسم المستخدم من STDIN |
| `2-read_file.js` | `countStudents` بقراءة متزامنة |
| `3-read_file_async.js` | `countStudents` بقراءة غير متزامنة ترجع Promise |
| `4-http.js` | سيرفر `http` بسيط على المنفذ 1245 |
| `5-http.js` | سيرفر `http` مع مسار `/students` |
| `6-http_express.js` | سيرفر Express بسيط |
| `7-http_express.js` | سيرفر Express مع مسار `/students` |
| `full_server/utils.js` | `readDatabase` ترجع Promise بكائن الحقول |
| `full_server/controllers/AppController.js` | `getHomepage` |
| `full_server/controllers/StudentsController.js` | `getAllStudents`, `getAllStudentsByMajor` |
| `full_server/routes/index.js` | ربط المسارات بالـ controllers |
| `full_server/server.js` | سيرفر Express منظّم على المنفذ 1245 |

## التشغيل

```bash
npm install
node 0-main.js
node 5-http.js database.csv
npm run dev          # full_server عبر babel-node + nodemon
npm run check-lint
```

## أمثلة الطلبات

```bash
curl localhost:1245                  # Hello Holberton School!
curl localhost:1245/students         # قائمة الطلاب لكل حقل
curl localhost:1245/students/SWE     # List: Guillaume, Joseph, Paul, Tommy
curl localhost:1245/students/French  # 500 Major parameter must be CS or SWE
```
