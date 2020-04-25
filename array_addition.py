

class ArrayAddition:

    def get_output_array(self, input_list):
        output_list = [0] * len(input_list)
        carry_over = 1
        for pos, num in reversed(list(enumerate(input_list))):
            temp = num + carry_over
            if temp > 9:
                output_list[pos] = 0
                carry_over = 1
            else:
                output_list[pos] = temp
                carry_over = 0
        if carry_over == 1:
            output_list = [1] + output_list
        print(output_list)
        return output_list
