# یادداشت نسخهٔ برنامهٔ مشتری

نسخه و کد نصب:

```text
1.1.15
versionCode: 21
```

این نسخه بخش هزینه‌ها را از برنامه حذف می‌کند.

بخش «قیمت و هزینه‌ها» و همهٔ محاسبه‌های درون‌برنامه‌ای برداشته شدند. برنامه دیگر جدول نرخ، محاسبه‌گر مبلغ، انتخاب سرعت شبکه و انتخاب برچسب یا تحویل حضوری ندارد و هیچ عدد هزینه‌ای نمی‌سازد. جدول هزینه و برآورد قیمت فقط در صفحهٔ هزینه‌های سایت است.

ورودی‌های حذف‌شده: دکمهٔ «قیمت و هزینه‌ها» در صفحهٔ نخست و در فهرست «اطلاعات پرداخت و تماس». صفحهٔ آفلاین هزینه‌ها هم از بستهٔ برنامه برداشته شد، پس متن قدیمی آن دیگر در برنامه خوانده نمی‌شود.

دلیل: یک مدل هزینه در یک جا. پیش‌تر همان فرمول در سایت و در برنامه تکرار می‌شد و هر تغییر قیمت باید در دو جا هم‌زمان درست می‌شد؛ اگر یکی عقب می‌ماند، عدد برنامه با سایت فرق می‌کرد.

بقیهٔ کارها تغییر نکرده است: خواندن برچسب NFC، استعلام با سریال یا آدرس عمومی، کارت نتیجه با موجودی در بالا، سه کاوشگر برای آدرس ناشناس، و صفحه‌های آفلاین راهنما، شرایط، پرداخت و امنیت. هر پیوند بیرونی مثل قبل از دیالوگ رضایت رد می‌شود و هیچ‌چیز خودکار باز یا ارسال نمی‌شود.

نکتهٔ مهم: این برنامه دیگر هیچ برآورد قیمتی بدون اینترنت نمی‌دهد.

This release removes the costs section from the app.

The "price and costs" screen and all in-app cost arithmetic are gone. The app no longer shows a rate table, a custom-amount calculator, a network-speed selector, or the tag and hand-delivery toggles, and it produces no cost figure of its own. The cost table and the price estimate live only on the site's costs page.

Removed entry points: the "price and costs" button on the home screen and in the "payment and contact" group. The offline costs page was also dropped from the bundle, so its old text is no longer read by the app.

Rationale: one cost model in one place. The same formula used to exist in both the site and the app, so every price change had to land correctly in two places; when one lagged behind, the app disagreed with the site.

Everything else is unchanged: NFC tag reading, lookup by serial or public address, the result card with the balance first, the three explorers for an unknown address, and the offline guide, terms, payment and security pages. Every external link still passes through the consent dialog and nothing opens or sends automatically.

Important: the app now gives no price estimate at all without internet access.

این یادداشت فقط تغییرات نسخهٔ ۱.۱.۱۵ را ثبت می‌کند و به معنی ساخته‌شدن، امضاشدن یا انتشار فایل APK جدید نیست.

## شرط انتشار و مرز شواهد

اجرای دستی امضاشده باید پیش از ساخت برچسب عمومی موفق شود. آزمون میزبان، بررسی ایستا و وابستگی سخت‌گیرانه در هر دو نوع ساخت اجرا می‌شوند. شناسهٔ بسته و گواهی ثابت تغییر نکرده‌اند. گزارش اجرای واقعی و فایل دانلودشده معیار پذیرش‌اند؛ این یادداشت به‌تنهایی موفقیت آن‌ها را اعلام نمی‌کند.

آزمون خودکار این دور: ۶۱ آزمون منبع پایتون سبز، و ساخت `:core:test` به‌همراه `:app:assembleDebug` و `:app:assembleDebugAndroidTest` موفق. آزمون شبیه‌ساز و گوشی واقعی در این دور اجرا نشد؛ حذف یک بخش، رفتار میدان NFC یا چیدمان گوشی را اثبات نمی‌کند.
