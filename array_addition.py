

class ArrayAddition:

    def get_added_array(self, input_list, add_by=1):
        output_list = [0] * len(input_list)
        carry_over = add_by
        for pos, num in reversed(list(enumerate(input_list))):
            temp = num + carry_over
            if temp > 9:
                output_list[pos] = temp % 10
                carry_over = temp // 10
            else:
                output_list[pos] = temp
                carry_over = 0
        if carry_over == 1:
            output_list = [1] + output_list
        print(f"Input array = {input_list} Output array = {output_list}")
        return output_list
