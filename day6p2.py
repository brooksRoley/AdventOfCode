import sys
# To fix the communication system,
# add a subroutine to detect a start-of-packet marker in the datastream
# In the protocol being used by the Elves,
# the start of a packet is indicated by
# a sequence of four characters that are all different.

#  marker after character 19
# ds = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'

# #  marker after character 23
# ds = 'bvwbjplbgvbhsrlpgdmjqwftvncz'

# #  marker after character 23
# ds = 'nppdvjthqldpwncqszvftbrmjlhg'

# #  marker after character 29
# ds = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'

# #  marker after character 26
# ds = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'

ds = 'bgdbdsbsbsttldddzzwnzzmpzmmzmqqcgglrglgbbbtmtddrssjtjqqtrtqtqppcvcddswdwbwlblfljfljlhhpchcfcgfcfwfllfccjlcjllbvbgglccznzrnzzvfzvffvzvccnwnnrtrqtttzmmndnqnvvlwvvgcclplccbggcscqscqcnndwdlwlvlffdssrzrtttbvvqttfdfrddhthbblnlmlmqmhhpvpcpwpccmdddbcbcgctggsstwwbcwwqllchlcccfwccvjcjhhvggnvvcssjwjhhdvdhdcdhdqhhwrwcrwcrrjzjccqhhvnnrppsqqplqqcvczzlpprlrqqvpvwwstwwzqqsnqqsrqrlqlggzztzhhvbbcncwnwhwbbqpbqpqdqsqjqrjrddpjpwwvlwlnwwmpwwnmmzgzqqdcdnnqllghhzwhwwggljjwswgwffsbffbggzfzcfzczpptrrnwrrcqqcwqqdttzqzjzqqltlggwlglgwgrgfgnffgqffnlntlnlccjwjfjnfjnffqvfqfcfsslwswfwvfwfvflfhhntngnhggqbbsggchghfggcmgmsggshsmmqffjpjnngwwftwffgqqvmqqslqslqqdzqzhzbhhdzhhllnzzlmzzltlwwsmswwtswtssvqsqhssfdsdtdjdqqqrffqjffrzrppjpgjjpgpmmzbbrcbbprbpbnpbpcpsspqqfggclcpczzngznzvzlvvcwvwcwdwcddhdbdwdhwhllpjllrmmhbmbgmgmpmhpmpqmpprggvsgvsvbsbbqbmmjdjfddsnnqpnnphppsbpsbpsprpjjqhhvrhvvdhdjhdhwdhhdjjrlrbbzhbbjljhllttrccbdbffznnfmnfnvfvrvbblmltlmmlbmmdqmqnmqqmmhchvcvpccnrccqhccshchshzshschcffpwwbdbqbbjhbhmbhmmzzzcscddbsbnnpzpfzzrfrlrmmzzhshbbtjtbtzbbddrwwhchvhtvvmhvmmwssqqzrzdrdqqntnjnrjrbbgqgzgbzgbzgbzgbbqtbbbqjjgvglvlzlqlbbjwjddjtjbjffcsfsnsnpspgpnnglnngrgqgbqgqtgtfggczzmbbvqqrssdqssgrssdzzvjvccbbgcgppgwwtmwwrnwnfwwnnzmzvvvmnnvdddrmrbrtbrbrvrqqcbbgjgfjfcfttgrrjmrmrttbnnsrnsnzsnzztmtgtjgjljdjtjrtrddtbtjbtjbtthhtmmllngnhgnnhthssgffljlnjllfvlvslvsvwvcvfccgqqtsqtqggbjbtjjtjvjtvtvddttqzqczzcvvdtvthvvfrfmrrclrlflbbhhcllfbbcwwgmwmnmpmgpptnpnjpnjjbqjqjddfdfjjpzzjnnvzzwtwpwfppzhphbbmsbmsbmbqqfpfsscttfrtrzzrznrrrbgbdbtdbdjjsmjmttlbtthbttrprpjppsbsjbjcbclchlhhlttntznnzfnfgnncsncnmmdndnlnclnndqnqssbsjbbrzrtzztszzvnznqqpnpbpnpvnpnhpphvpvfvhhrvhrrpttctjcjvcvzcvcscttqptpffscfsccqhchhdcdczcnzcncnhccfrrbprpbpqppdccjhjvjmjpjmpjjvfvrrwppgjgjjdgdmgdggcpccbrrgssbsjbsjsfscfcvvcrvcrcttbtffpqphpchclccwhcwcbwccbzzlvzvffbrbrbjbwjjqvgtcfnhtjvrcwbfjdbvgtqbvmbtscwzrwdfmwtjvswgrvncmftgmppvlcwjpnpffggrmvgtfqgqmhbhpslfwdfvfmbfndrmgfhdbbtdgvnslzpdfvdttqjpcnbzsjcvrprgrhpglwfwtdcbgdsjhnqjntjnsjcgwccjnvvngfpvqwvnclcsvhmwsrccvbjnnrjspwqdvjpfnfvbsslngzpdgjrcsnqfvdlsqdhdllcndshglztgrrjnptqfvllshmhbgdszvmvqdntpgzdvhstgrppwpdtdqvzsfgqfrgmmjqcsjhvrlmnjvfjghlvwbnqcggpqtrjztfzshnqpzznvlqcmnzvrwqlcbnbpwmljpvdzhbvbgtdjlzflsvzlcqdnsgzfjlccvjclqlzdhqzzrscttjmrvjvcqzvtzqlmsssnfcfmvcgmqjjwdnhtvlqrgdvlbbrffmrpnfsmwwwbnwclrgbfnzlbqvjfqjlfvfnfrhdqstddwnwrmsdnvzwfjfgpwcrfqqzbdwwtzprvqtgvtzbttlhcdczlhvlgrbptztswftvnjmgrnbwpfwnztvqmqbznvnllgjmqrwprvwtnptlbfwbblzsblptwpdwgcvwsbmbrtqfvjsbzfvsfvpwfwbnnfcsddhsnwnvvqthjdgvzgjprtqmvhdqjqhgqppqqcpzfcwzcmrslftgrvbvdsdgfzfmvvcqzcszfwdvghdnlwwpddzdsqsdqvvrwhphbqvcbjbtnqgnqqdsqcmrllhmdvpffnqmrgfddjbrjwflshzswvjtmqgqmzvcnlctvdpjhzzlgpzgprjncrscnlmdhvdqpfllsqgstmssvlzmrtjmgwppfqjsrfmlnszdnhngzhtbbnsnvmtzpfsdcsvsvvjnfnzhrzmvlhrbslrsbgwwcvrzpgcnmjqnvgmzmlvpccrmggtzzhsdtbbcdnpdlnbztgjhttmqdhjphcrbgjtctqmgbfmflgqztztcjqvgsscrmwfbvnrnbgbjgqmwdzhwwnddwgrprhvlgftcbnwjqmcgczpbhfqcqzdbdwhmzfmgvcjdsfzdbrzjjvfrvftdblnlhpbqvdprnsjdpznbbgqpgnnjmcnsbszfwblthtwlwrdphjltclmqnbpcgngdnfpltttsrvdmhrcvlqfplqmqvslwgcbrwrmchscczrfgspwjtdqtlbddbsclrlbmhdzqdrgjfsgldfjmgcglbgjhmghntndqcbgqwmdvczbwgcctzvcrsqqctwwddfhhfhwlsrsljpnrlqtbdzprjbfrjgztwbpnfqnlftzcgrpmpcnljhscfbsqzbsgwqcgbvctnhswhrsmwjgcccdsnbscwllmpstpnrccjspnjqmtgcsgbjzpfvzjrhlvnfblqmcmgcrvnpchwhlsqsbhzhsgdvwmdcwphwccvzmmqqjrvqwphbnmddzcmggmbsqrhbcqmdlgvccbhhmhwdjhhhcwnffthmgfhpltqbhnvdqfrzjdvlppqhzfdgbzbrtfllsbvjjcgbwsbcmfrbjtvzqsntzdzprnpmfpfpgmfprlbcdqbdzjsfjbtczdpdnhlwdhmwsjtvmztbhdbbdgvrtbqsqbsnwjjhlslzcblrwlfpzqlvdvmgqhrpjmbjbntmjsjvgsmdsnctlgtnlqgfvhwqbjbrczpfzmzwgvrphfmnnhrlzwzgthzqnzzmptppzdszlcpjjvbpjbtjfrqtbnpnwsdglbbjftvngcghjlnsqwspmmfdpslsmqtpngbtvvrvbqqdsphfhvsnmhprfclnjmfrtqnlqcbmfrggbstwdbwsvtpvflvfgqltmqjpnfclbwtlwhmqrmzcrbztstgpjrdsnwpqrcnvvnnnszlrtpqjtsnbjrdcthrzrtccgcvnnlzfjlcdnzzqclvtncjbznrlpnzhvcwmrfrzpcldfmfzfpchlmddgvcfdqdhzzdtwhsfcvsthtmqgvhzdpjcgwsmrvwsnqmhdnfqdrrnmjwcpjjftfdhvwrwwtvptzfrmgffdcrhvcmccfqctswzzmlsjvdjzgjgndhmmrwvwmmtrnpgsnmtcqdbdpqjmcddcrbcfmmccnvsfhwtvfhsjfmlfttspfghpfggrffnrwjggqwggrmpzscprvdzmzhwjjcsmpsltzwgchttwpngrlptprqnjzzpbpbcvrclggtqwlcwdpjpnjrhtgqwsvhsswwqtlnglnqnvffrgmlbzthvnhrzvsvclgdmmjzrpfv'

for i in range(len(ds)):
    x = set(ds[i:i+14])
    if len(x) == 14:
        print(i+14)
        sys.exit("The sequence stopped")
