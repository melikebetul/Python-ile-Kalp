# Python ile Kalp Yapımı

Python'da kütüphane kullanımı ve syntax öğrenimi için küçük ve tatlı bir örnek olarak kalp yapalım.
İlk olarak bir python dosyası oluşturalım ve importlarımızı yaparak başlayalım. Bu projede çizimler için kullanılan Turtle kütüphanesini kullanacağız. 

Çizeceğimiz şekilde kıvrımlar olduğu için kıvrımlar oluşturmalıyız ve bu kıvrımları sık sık kullanacağımızdan teker teker yazmaktansa, curve() fonksiyonunu yazarak işimizi kolaylaştıracağız. Fonksiyonumuza, kaçıncı pikselde olduğu bize lazım olacağı için bir parametre veriyoruz. Sonrasında for döngüsüyle bir kıvrım oluşturuyoruz ve her seferinde piksel sayımızı bir arttırıyoruz. En son ise kaçıncı pikselde kaldığımızı geri döndürüyoruz. 
    
Şimdi düz çizgi için bir fonksiyon oluşturalım. Her seferinde kaç piksel ileri gideceğimiz değişkenlik gösterdiği için onu da ayrı bir parametre olarak alıyoruz. Bir sağ bir sol yapmamızın sebebi ise kıvrım ile düzgü çizgi arasındaki hız farkı. Sonrasında curve() fonksiyonundaki gibi kaçıncı pikselde olduğumuzu geri döndürüyoruz. 

Şimdi ise sıra kalbizi asıl olarak çizecek olan heart() fonksiyonunda. Fonksiyonumuzda ilk olarak pembe rengini kullanacağımızı belirtiyoruz. Açılar vererek az önce oluşturduğumuz fonksiyonlarımızı kullanıyor ve bir kalp şekli çiziyoruz. En son ise içini dolduruyoruz. Şuan bu kod dosyamızda heart fonksiyonunu çağırarak bir kalp şekli çizilmesini sağlayabiliriz. 
 
Son olarak kalbimizin içine yazı yazmak için bir fonksiyon yazacağız. Bu fonksiyonumuzu txt() olarak adlandıralım. Kalbi çizme ve içini doldurma işlemiz bittikten ilk olarak kalemimizi yukarı kaldırıyoruz, ayarladığımız pozisyona getirip tekrar aşağı bırakıyoruz. Sonrasında seçtiğimiz renk ile belirlediğimiz yazıyı, verdiğimiz özelliklere göre yazmasını istiyoruz.

Test Zamanı!
Fonksiyonlarımızı çağırarak ve sonrasında kalemi kaldırarak kalbimizi çizme işlemimizi gerçekleştirmiş oluyoruz.
