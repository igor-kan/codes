; ModuleID = 'algorithms/02_c/math/miller_rabin.c'
source_filename = "algorithms/02_c/math/miller_rabin.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@miller_rabin.bases = internal unnamed_addr constant [7 x i64] [i64 2, i64 325, i64 9375, i64 28178, i64 450775, i64 9780504, i64 1795265022], align 16
@__const.main.primes = private unnamed_addr constant [3 x i64] [i64 1000000007, i64 2147483647, i64 999999999989], align 16
@__const.main.composites = private unnamed_addr constant [3 x i64] [i64 1000000005, i64 2147483649, i64 3000000021], align 16
@.str = private unnamed_addr constant [32 x i8] c"miller_rabin(primes[i]) == true\00", align 1
@.str.1 = private unnamed_addr constant [36 x i8] c"algorithms/02_c/math/miller_rabin.c\00", align 1
@__PRETTY_FUNCTION__.main = private unnamed_addr constant [15 x i8] c"int main(void)\00", align 1
@.str.2 = private unnamed_addr constant [37 x i8] c"miller_rabin(composites[i]) == false\00", align 1
@str = private unnamed_addr constant [58 x i8] c"[C Miller-Rabin] Deterministic 64-bit primality verified.\00", align 1

; Function Attrs: nofree norecurse nosync nounwind sspstrong memory(none) uwtable
define dso_local noundef zeroext i1 @miller_rabin(i64 noundef %0) local_unnamed_addr #0 {
  %2 = icmp ult i64 %0, 2
  br i1 %2, label %67, label %3

3:                                                ; preds = %1
  %4 = icmp ult i64 %0, 4
  br i1 %4, label %67, label %5

5:                                                ; preds = %3
  %6 = and i64 %0, 1
  %7 = icmp eq i64 %6, 0
  br i1 %7, label %67, label %8

8:                                                ; preds = %5
  %9 = add nsw i64 %0, -1
  br label %13

10:                                               ; preds = %13
  %11 = zext i64 %0 to i128
  %12 = icmp eq i32 %14, 0
  br label %20

13:                                               ; preds = %8, %13
  %14 = phi i32 [ %17, %13 ], [ 0, %8 ]
  %15 = phi i64 [ %16, %13 ], [ %9, %8 ]
  %16 = lshr exact i64 %15, 1
  %17 = add nuw nsw i32 %14, 1
  %18 = and i64 %15, 2
  %19 = icmp eq i64 %18, 0
  br i1 %19, label %13, label %10, !llvm.loop !9

20:                                               ; preds = %10, %64
  %21 = phi i64 [ 0, %10 ], [ %65, %64 ]
  %22 = getelementptr inbounds nuw i64, ptr @miller_rabin.bases, i64 %21
  %23 = load i64, ptr %22, align 8, !tbaa !11
  %24 = urem i64 %23, %0
  %25 = icmp eq i64 %24, 0
  br i1 %25, label %67, label %26

26:                                               ; preds = %20, %40
  %27 = phi i64 [ %42, %40 ], [ 1, %20 ]
  %28 = phi i64 [ %45, %40 ], [ %24, %20 ]
  %29 = phi i64 [ %46, %40 ], [ %16, %20 ]
  %30 = and i64 %29, 1
  %31 = icmp eq i64 %30, 0
  br i1 %31, label %32, label %34

32:                                               ; preds = %26
  %33 = zext i64 %28 to i128
  br label %40

34:                                               ; preds = %26
  %35 = zext i64 %27 to i128
  %36 = zext i64 %28 to i128
  %37 = mul nuw nsw i128 %36, %35
  %38 = urem i128 %37, %11
  %39 = trunc nuw i128 %38 to i64
  br label %40

40:                                               ; preds = %34, %32
  %41 = phi i128 [ %33, %32 ], [ %36, %34 ]
  %42 = phi i64 [ %27, %32 ], [ %39, %34 ]
  %43 = mul nuw nsw i128 %41, %41
  %44 = urem i128 %43, %11
  %45 = trunc nuw i128 %44 to i64
  %46 = lshr i64 %29, 1
  %47 = icmp eq i64 %46, 0
  br i1 %47, label %48, label %26, !llvm.loop !13

48:                                               ; preds = %40
  %49 = icmp eq i64 %42, 1
  %50 = icmp eq i64 %42, %9
  %51 = select i1 %49, i1 true, i1 %50
  br i1 %51, label %64, label %52

52:                                               ; preds = %48
  br i1 %12, label %67, label %56

53:                                               ; preds = %56
  %54 = add nuw i32 %57, 1
  %55 = icmp eq i32 %57, %14
  br i1 %55, label %67, label %56, !llvm.loop !14

56:                                               ; preds = %52, %53
  %57 = phi i32 [ %54, %53 ], [ 1, %52 ]
  %58 = phi i64 [ %62, %53 ], [ %42, %52 ]
  %59 = zext i64 %58 to i128
  %60 = mul nuw nsw i128 %59, %59
  %61 = urem i128 %60, %11
  %62 = trunc nuw i128 %61 to i64
  %63 = icmp eq i64 %9, %62
  br i1 %63, label %64, label %53

64:                                               ; preds = %56, %48
  %65 = add nuw nsw i64 %21, 1
  %66 = icmp eq i64 %65, 7
  br i1 %66, label %67, label %20, !llvm.loop !15

67:                                               ; preds = %52, %64, %20, %53, %5, %3, %1
  %68 = phi i1 [ false, %5 ], [ false, %1 ], [ true, %3 ], [ false, %53 ], [ false, %52 ], [ true, %64 ], [ true, %20 ]
  ret i1 %68
}

; Function Attrs: nounwind sspstrong uwtable
define dso_local noundef i32 @main() local_unnamed_addr #1 {
  br label %3

1:                                                ; preds = %128
  %2 = tail call i32 @puts(ptr nonnull dereferenceable(1) @str)
  ret i32 0

3:                                                ; preds = %0, %128
  %4 = phi i64 [ 0, %0 ], [ %129, %128 ]
  %5 = getelementptr inbounds nuw i64, ptr @__const.main.primes, i64 %4
  %6 = load i64, ptr %5, align 8, !tbaa !11
  %7 = add nsw i64 %6, -1
  br label %11

8:                                                ; preds = %11
  %9 = zext i64 %6 to i128
  %10 = icmp eq i32 %12, 0
  br label %18

11:                                               ; preds = %11, %3
  %12 = phi i32 [ %15, %11 ], [ 0, %3 ]
  %13 = phi i64 [ %14, %11 ], [ %7, %3 ]
  %14 = lshr exact i64 %13, 1
  %15 = add nuw nsw i32 %12, 1
  %16 = and i64 %13, 2
  %17 = icmp eq i64 %16, 0
  br i1 %17, label %11, label %8, !llvm.loop !9

18:                                               ; preds = %62, %8
  %19 = phi i64 [ 0, %8 ], [ %63, %62 ]
  %20 = getelementptr inbounds nuw i64, ptr @miller_rabin.bases, i64 %19
  %21 = load i64, ptr %20, align 8, !tbaa !11
  %22 = urem i64 %21, %6
  %23 = icmp eq i64 %22, 0
  br i1 %23, label %66, label %24

24:                                               ; preds = %18, %38
  %25 = phi i64 [ %40, %38 ], [ 1, %18 ]
  %26 = phi i64 [ %43, %38 ], [ %22, %18 ]
  %27 = phi i64 [ %44, %38 ], [ %14, %18 ]
  %28 = and i64 %27, 1
  %29 = icmp eq i64 %28, 0
  br i1 %29, label %30, label %32

30:                                               ; preds = %24
  %31 = zext i64 %26 to i128
  br label %38

32:                                               ; preds = %24
  %33 = zext i64 %25 to i128
  %34 = zext i64 %26 to i128
  %35 = mul nuw nsw i128 %34, %33
  %36 = urem i128 %35, %9
  %37 = trunc nuw i128 %36 to i64
  br label %38

38:                                               ; preds = %32, %30
  %39 = phi i128 [ %31, %30 ], [ %34, %32 ]
  %40 = phi i64 [ %25, %30 ], [ %37, %32 ]
  %41 = mul nuw nsw i128 %39, %39
  %42 = urem i128 %41, %9
  %43 = trunc nuw i128 %42 to i64
  %44 = lshr i64 %27, 1
  %45 = icmp eq i64 %44, 0
  br i1 %45, label %46, label %24, !llvm.loop !13

46:                                               ; preds = %38
  %47 = icmp eq i64 %40, 1
  %48 = icmp eq i64 %40, %7
  %49 = select i1 %47, i1 true, i1 %48
  br i1 %49, label %62, label %50

50:                                               ; preds = %46
  br i1 %10, label %65, label %54

51:                                               ; preds = %54
  %52 = add nuw i32 %55, 1
  %53 = icmp eq i32 %55, %12
  br i1 %53, label %65, label %54, !llvm.loop !14

54:                                               ; preds = %50, %51
  %55 = phi i32 [ %52, %51 ], [ 1, %50 ]
  %56 = phi i64 [ %60, %51 ], [ %40, %50 ]
  %57 = zext i64 %56 to i128
  %58 = mul nuw nsw i128 %57, %57
  %59 = urem i128 %58, %9
  %60 = trunc nuw i128 %59 to i64
  %61 = icmp eq i64 %7, %60
  br i1 %61, label %62, label %51

62:                                               ; preds = %54, %46
  %63 = add nuw nsw i64 %19, 1
  %64 = icmp eq i64 %63, 7
  br i1 %64, label %66, label %18, !llvm.loop !15

65:                                               ; preds = %50, %51
  tail call void @__assert_fail(ptr noundef nonnull @.str, ptr noundef nonnull @.str.1, i32 noundef 61, ptr noundef nonnull @__PRETTY_FUNCTION__.main) #4
  unreachable

66:                                               ; preds = %62, %18
  %67 = getelementptr inbounds nuw i64, ptr @__const.main.composites, i64 %4
  %68 = load i64, ptr %67, align 8, !tbaa !11
  %69 = add nsw i64 %68, -1
  br label %73

70:                                               ; preds = %73
  %71 = zext i64 %68 to i128
  %72 = icmp eq i32 %74, 0
  br label %80

73:                                               ; preds = %73, %66
  %74 = phi i32 [ %77, %73 ], [ 0, %66 ]
  %75 = phi i64 [ %76, %73 ], [ %69, %66 ]
  %76 = lshr exact i64 %75, 1
  %77 = add nuw nsw i32 %74, 1
  %78 = and i64 %75, 2
  %79 = icmp eq i64 %78, 0
  br i1 %79, label %73, label %70, !llvm.loop !9

80:                                               ; preds = %124, %70
  %81 = phi i64 [ 0, %70 ], [ %125, %124 ]
  %82 = getelementptr inbounds nuw i64, ptr @miller_rabin.bases, i64 %81
  %83 = load i64, ptr %82, align 8, !tbaa !11
  %84 = urem i64 %83, %68
  %85 = icmp eq i64 %84, 0
  br i1 %85, label %127, label %86

86:                                               ; preds = %80, %100
  %87 = phi i64 [ %102, %100 ], [ 1, %80 ]
  %88 = phi i64 [ %105, %100 ], [ %84, %80 ]
  %89 = phi i64 [ %106, %100 ], [ %76, %80 ]
  %90 = and i64 %89, 1
  %91 = icmp eq i64 %90, 0
  br i1 %91, label %92, label %94

92:                                               ; preds = %86
  %93 = zext i64 %88 to i128
  br label %100

94:                                               ; preds = %86
  %95 = zext i64 %87 to i128
  %96 = zext i64 %88 to i128
  %97 = mul nuw nsw i128 %96, %95
  %98 = urem i128 %97, %71
  %99 = trunc nuw i128 %98 to i64
  br label %100

100:                                              ; preds = %94, %92
  %101 = phi i128 [ %93, %92 ], [ %96, %94 ]
  %102 = phi i64 [ %87, %92 ], [ %99, %94 ]
  %103 = mul nuw nsw i128 %101, %101
  %104 = urem i128 %103, %71
  %105 = trunc nuw i128 %104 to i64
  %106 = lshr i64 %89, 1
  %107 = icmp eq i64 %106, 0
  br i1 %107, label %108, label %86, !llvm.loop !13

108:                                              ; preds = %100
  %109 = icmp eq i64 %102, 1
  %110 = icmp eq i64 %102, %69
  %111 = select i1 %109, i1 true, i1 %110
  br i1 %111, label %124, label %112

112:                                              ; preds = %108
  br i1 %72, label %128, label %116

113:                                              ; preds = %116
  %114 = add nuw i32 %117, 1
  %115 = icmp eq i32 %117, %74
  br i1 %115, label %128, label %116, !llvm.loop !14

116:                                              ; preds = %112, %113
  %117 = phi i32 [ %114, %113 ], [ 1, %112 ]
  %118 = phi i64 [ %122, %113 ], [ %102, %112 ]
  %119 = zext i64 %118 to i128
  %120 = mul nuw nsw i128 %119, %119
  %121 = urem i128 %120, %71
  %122 = trunc nuw i128 %121 to i64
  %123 = icmp eq i64 %69, %122
  br i1 %123, label %124, label %113

124:                                              ; preds = %116, %108
  %125 = add nuw nsw i64 %81, 1
  %126 = icmp eq i64 %125, 7
  br i1 %126, label %127, label %80, !llvm.loop !15

127:                                              ; preds = %124, %80
  tail call void @__assert_fail(ptr noundef nonnull @.str.2, ptr noundef nonnull @.str.1, i32 noundef 62, ptr noundef nonnull @__PRETTY_FUNCTION__.main) #4
  unreachable

128:                                              ; preds = %112, %113
  %129 = add nuw nsw i64 %4, 1
  %130 = icmp eq i64 %129, 3
  br i1 %130, label %1, label %3, !llvm.loop !16
}

; Function Attrs: cold noreturn nounwind
declare void @__assert_fail(ptr noundef, ptr noundef, i32 noundef, ptr noundef) local_unnamed_addr #2

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr noundef readonly captures(none)) local_unnamed_addr #3

attributes #0 = { nofree norecurse nosync nounwind sspstrong memory(none) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #2 = { cold noreturn nounwind "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { nofree nounwind }
attributes #4 = { cold noreturn nounwind }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}
!llvm.errno.tbaa = !{!5}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 2}
!4 = !{!"clang version 22.1.8"}
!5 = !{!6, !6, i64 0}
!6 = !{!"int", !7, i64 0}
!7 = !{!"omnipotent char", !8, i64 0}
!8 = !{!"Simple C/C++ TBAA"}
!9 = distinct !{!9, !10}
!10 = !{!"llvm.loop.mustprogress"}
!11 = !{!12, !12, i64 0}
!12 = !{!"long", !7, i64 0}
!13 = distinct !{!13, !10}
!14 = distinct !{!14, !10}
!15 = distinct !{!15, !10}
!16 = distinct !{!16, !10}
