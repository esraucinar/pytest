# pytest
                                PyTest- Decorators
PyTest, Python'da kullanılan, yazılan programları test eden bir test çerçevesidir. 
PyTest'in en önemli özelliği hata ayıklayıcı olarak kullanılmasıdır. 
Python'da decorator'lar, işlevleri veya testleri genişletmek, 
işlevleri işaretlemek veya testlerin davranışını değiştirmek için kullanılan özel işaretçi nitelikleridir.
Pytest'te sık kullanılan decorator'lar şunlardır: 

@pytest.fixture: Bu, testler arasında durum paylaşımını sağlayan ve gerekli kaynakları testlere sağlayan fixture'ları tanımlar.

@pytest.mark.parametrize: Aynı test fonksiyonunu farklı girişlerle tekrar tekrar çalıştırmanıza olanak tanır, böylece testlerinizi çeşitli senaryolarla kontrol edebilirsiniz. 

@pytest.mark.skip: Belirli bir testin atlanmasını sağlar. Örneğin, henüz hazır olmayan veya geçici olarak kullanılmayan testleri işaretlemek için kullanılır. 

@pytest.mark.xfail: Beklenen başarısız test durumlarını işaretlemek için kullanılır. Yani, testin başarısız olmasını beklediğinizi belirtir. 

Bu decorator'lar, testlerinizi işaretlemek, düzenlemek veya davranışlarını değiştirmek için kullanılır. 
Pytest'te kullanıldıklarında testlerinizi daha esnek ve organize etmenizi daha kolay hale getirirler. """
