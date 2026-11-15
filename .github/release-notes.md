# یادداشت نسخهٔ برنامهٔ مشتری

نسخه و کد نصب:

```text
1.1.14
versionCode: 20
```

این نسخه کارت نتیجهٔ استعلام را بازچینش می‌کند و آدرس ناشناس را قابل بررسی می‌کند.

موجودی حالا اول کارت می‌آید: موجودی تأییدشده به ساتوشی و معادل بیت‌کوین آن، بعد تغییر در انتظار، بعد آدرس، بعد سریال. پیش‌تر موجودی پایین‌تر از آدرس و کد تصویری بود و کاربر گوشی مجبور بود اسکرول کند. اعداد موجودی درشت‌تر و با فاصلهٔ یکنواخت نمایش داده می‌شوند تا کوچک‌ترین مقدار هم گم نشود.

اگر آدرس عمومی را وارد کنید و آن آدرس در فهرست ما نباشد، برنامه دیگر فقط یک خط خطا نشان نمی‌دهد. کارت می‌گوید این آدرس در فهرست ما ثبت نشده است، خود آدرس را نشان می‌دهد، و سه پیوند کاوشگر برای همان آدرس می‌دهد: مم‌پول، بلاک‌استریم و بلاک‌چین. هر پیوند مثل همیشه از دیالوگ رضایت رد می‌شود و هیچ‌کدام خودکار باز نمی‌شود. برای آدرس ناشناس موجودی گرفته نمی‌شود و عدد صفر ساخته نمی‌شود.

بخش استعلام ساده‌تر شده است: اول شمارهٔ سریال با دکمهٔ اصلی، بعد آدرس عمومی، و یک خط توضیح که می‌گوید اگر آدرس در فهرست نباشد چه می‌بینید. ارتفاع کادرهای ورودی به ۴۸ واحد رسیده تا روی گوشی راحت لمس شوند.

هزینه‌ها: مواد پاکت پنج سنت (مهر سه، کاغذ یک و چاپ یک) همیشه حساب می‌شود. در ارسال پستی، پاکت شش سنت و پست هفتاد و پنج سنت هم می‌آید؛ در تحویل حضوری فقط همان مواد می‌ماند. برچسب دوازده سنت است. حداقل بسته از پانصد و یک ساتوشی شروع می‌شود و سقف جدول سه میلیون تومان است.

نرخ بیت‌کوین یک درصد کارمزد صرافی دارد، چون دو کارمزد نیم‌درصدی جدا پرداخت می‌شود: یکی هنگام خرید کوین و یکی هنگام تبدیل آن به بیت‌کوین. این یک درصد فقط یک بار روی نرخ اعمال می‌شود، نه روی اصل مبلغ. علاوه بر آن، کارمزد تبدیل دو سنت و کارمزد انتقال بیت‌کوین چهارصد و بیست‌وسه ساتوشی است. این دو به انتخاب سرعت شبکه وابسته نیستند؛ فقط هزینهٔ شبکهٔ تحویل با انتخاب اقتصادی، متوسط یا سریع عوض می‌شود. نرخ تتر تعدیل نمی‌شود.

برنامه پاسخ نرخ را پیش از نمایش اعتبارسنجی می‌کند و پاسخ ناسازگار را کنار می‌گذارد؛ هیچ قیمت صفر یا جایگزینی ساخته نمی‌شود. هر دو قرارداد هزینه را می‌شناسد: اگر سرور جدول قدیمی بدهد، همان را با مدل قدیم می‌خواند و کارمزد غایب را صفر فرض نمی‌کند.

دکمهٔ «قیمت و هزینه‌ها» از صفحهٔ نخست در دسترس است و گزینهٔ «ارسال پستی / حضوری» در همان صفحه انتخاب می‌شود.

خواندن برچسب: حالت خوانندهٔ NFC پس از خواندن روشن می‌ماند و فقط با خروج از صفحه آزاد می‌شود. اگر میدان در همان لحظه که برچسب روی گوشی است آزاد شود، اندروید لینک ذخیره‌شده روی برچسب را به مرورگر می‌دهد، این صفحه متوقف می‌شود و نتیجهٔ خواندن از دست می‌رود. هر خواندن نشانهٔ یکتای خودش را دارد و پاسخ دیررسِ خواندن قدیمی کنار گذاشته می‌شود.

This release reorders the lookup result card and makes an unknown address checkable.

The balance now comes first: confirmed sats and the BTC equivalent, then the pending delta, then the address, then the serial. Previously the balance sat below the address and the QR, so a phone user had to scroll for the number they came for. Balance values render larger with tabular figures so a small amount is never lost.

If you enter a public address that is not in our list, the app no longer stops at an error line. The card says the address is not registered with us, shows the address, and offers the three public explorers for it — mempool.space, blockstream.info and blockchain.com. Every link still goes through the consent dialog and nothing opens automatically. No balance is fetched for an unknown address and no zero is invented.

The lookup section is simpler: the serial first with the primary button, the address second, and one muted line explaining what happens when an address is not in our list. Input heights are raised to 48dp for comfortable touch.

The bitcoin rate carries a 1% exchange markup because two separate 0.5% fees are paid (buying the coin, then converting it to bitcoin); the markup is applied once to the rate, never to the principal. Two fixed fees are added: a two-cent conversion charge and a 423-satoshi bitcoin transfer. Neither depends on the selected network speed — only the delivery network fee follows economy/medium/fast. The tether rate is not marked up. Card materials 0.05 USD are always charged, postal delivery adds a 0.06 USD envelope and 0.75 USD postage, hand delivery drops only those two, and the tag is 0.12 USD. The smallest package starts at 501 satoshis and the table ceiling is 3,000,000 toman. Every market response is validated before it is shown and a mismatching response is dropped instead of being rendered with a zero or invented price. Both cost contracts are understood: an older server table is read with the legacy model rather than treating the absent fees as zero.

The costs screen is reachable from the home screen, and the postal/hand-delivery choice lives on that screen.

NFC reader mode now stays enabled after a read and is released only when the user leaves the screen. Releasing the field while the tag is still against the phone hands the tag's stored link to Android, which opens a browser, pauses this screen and loses the scan. Each scan carries its own immutable token, so a late callback from an older scan is dropped instead of overwriting a newer result or re-enabling a request the user cancelled. That guard lives in `core` and has behavioural unit tests, not only source-text assertions.

این یادداشت فقط تغییرات و شرط‌های بررسی نسخهٔ ۱.۱.۱۰ را ثبت می‌کند و به معنی ساخته‌شدن، امضاشدن یا انتشار فایل APK جدید نیست.

آزمون سیاست پنجره در همان دروازهٔ شبیه‌ساز میزبانی‌شده اجرا می‌شود. این آزمون روی پنجرهٔ واقعی شبیه‌ساز سیاست انتشار و راه‌اندازی فعالیت آزمایشی را بررسی می‌کند؛ اثبات اجرای بسته روی گوشی نیست.

## شرط انتشار و مرز شواهد

اجرای دستی امضاشده باید پیش از ساخت برچسب عمومی موفق شود. آزمون میزبان و بررسی ایستا و وابستگی سخت‌گیرانه در هر دو نوع ساخت اجرا می‌شوند. شناسهٔ بسته و گواهی ثابت تغییر نکرده‌اند. گزارش اجرای واقعی و فایل دانلودشده معیار پذیرش‌اند؛ این یادداشت به‌تنهایی موفقیت آن‌ها را اعلام نمی‌کند.

گوشی و تگ فیزیکی، ارتقای نصب تولیدی و حداقل نسخهٔ اندروید در این دور آزموده نشده‌اند. خواندن فیزیکی برچسب و رفتار میدان NFC روی گوشی واقعی تأیید نشده است؛ آزمون خودکار فقط منطق گارد را می‌سنجد. آزمون شبیه‌ساز با آزمون گوشی واقعی تفاوت دارد. نبود کلید معتبر باعث توقف می‌شود و هیچ کلیدی ساخته یا به دستگاه محلی منتقل نمی‌شود.
