# ES6 data manipulation

مشروع عن التعامل مع البيانات في JavaScript: `map`, `filter`, `reduce`،
والـ Typed Arrays، و `Set`، و `Map`.

## المفاهيم

| المفهوم | الشرح |
| --- | --- |
| `map` | يحوّل كل عنصر في المصفوفة ويرجع مصفوفة جديدة بنفس الطول |
| `filter` | يرجع مصفوفة جديدة فيها العناصر الي تحقق الشرط فقط |
| `reduce` | يجمّع كل العناصر في قيمة واحدة (مجموع، كائن، نص…) |
| `ArrayBuffer` / `DataView` | ذاكرة خام بحجم ثابت + طريقة لقراءة/كتابة بايتات فيها |
| `Set` | مجموعة قيم فريدة بدون تكرار |
| `Map` | قاموس مفتاح ← قيمة، وأي نوع يصلح كمفتاح |
| `WeakMap` | مثل `Map` بس مفاتيحه كائنات ويسمح بجمع القمامة |

## الملفات

| الملف | المهمة |
| --- | --- |
| `0-get_list_students.js` | يرجع مصفوفة كائنات الطلاب |
| `1-get_list_student_ids.js` | `map` لاستخراج الـ ids |
| `2-get_students_by_loc.js` | `filter` حسب المدينة |
| `3-get_ids_sum.js` | `reduce` لجمع الـ ids |
| `4-update_grade_by_city.js` | `filter` + `map` لإضافة الدرجات |
| `5-typed_arrays.js` | `ArrayBuffer` و `DataView` |
| `6-set.js` | إنشاء `Set` من مصفوفة |
| `7-has_array_values.js` | التحقق أن كل القيم موجودة في `Set` |
| `8-clean_set.js` | تجميع قيم `Set` تبدأ بنص معيّن |
| `9-groceries_list.js` | إنشاء `Map` للمشتريات |
| `10-update_uniq_items.js` | تعديل قيم `Map` عند الكمية 1 |

## التشغيل

```bash
npm install
npm run dev 0-main.js
npm run full-test
```
